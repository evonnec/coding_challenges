#!/a/wwwww/app/ocaml-script/prod/114.04/ocaml-script run

open Core.Std
open Csvlib

(* $ cat /a/zzz/group/yyy/readonly/scripts/books_CA/2016-12-02/depo_data.csv | awk -F, -v OFS="," '{print substr($2,1,length($2)),$4,$3}' | sort *)

(* let table_iter ~num_keys ~iterations = 
*   let table = Table.create ~size:num_keys () in 
*   let rec loop i = 
*     if i <= 0 then () 
*     else ( 
*       Hashtbl.change table (i mod num_keys) (fun current -> 
*         Some (1+~hashable:String.hashable (); *)

let hastbl_results csv db hash_table =
  let match_and_add ~key ~data =
    let filtered_data = match (String.Map.find csv key) with
      | None -> ["none"]
      | Some data_list -> data_list
    in
    let full_data = List.append data filtered_data in
    match (Hashtbl.add hash_table ~key ~data:full_data) with
    | `Ok -> ()
    | `Duplicate -> ()
  in
  return (String.Map.iter ~f:match_and_add db)

let main () =
  let print_to_csv hashtable filepath =
    let placehold_list =
      let pre_filtered_list ~key ~data target =
        let readin = In_channel.read_all "/a/zzz/group/yyy/readonly/scripts/books_CA/2016-12-01/depo_data.csv" in
        (* Core.Std.printf "Hi %s\n%!" readin *)
        let bny_data = String.split readin ~on:',' in
        let sym = List.nth_exn bny_data 1 in
        let c_date = List.nth_exn bny_data 2 in
        let uniq_date = Set.of_list ~comparator:Date.comparator uniq_date in
        let ttype = List.nth_exn bny_data 3 in
        List.append target [List.append [] data]
      in
      Hashtbl.fold hashtable ~init:[] ~f:filtered_list
    in
    List.append [[ "counter";
                   "sym";                   
                   "c_date";                   
                   "ttype";                   
                   "o_date";                   
                   "reason";                   
                   "country";                   
                   "cusip";                   
                   "timestmp";                   
                   "depo" ]] filtered_list
    in
    return (Csv.save ~separator:',' filepath filtered_list)

let insert_first t value =
  let new_elt = { prev = None; next = !t; value } in
  begin match !t with
  | Some old_first -> old_first.prev <- Some new_elt
  | None -> ()
  end;
  t := Some new_elt;
  new_elt

let insert_after elt value =
  let new_elt = { value; prev = Some elt; next = elt.next } in
  begin match elt.next with
  | Some old_next -> old_next.prev <- Some new_elt
  | None -> ()
  end;
  elt.next <- Some new_elt;
  new_elt

let remove t elt =
  let { prev; next; _ } = elt in
  begin match prev with
  | Some prev -> prev.next <- next
  | None -> t := next
  end;
  begin match next with
  | Some next -> next.prev <- prev;
  | None -> ()
  end;
  elt.prev <- None;
  elt.next <- None

let iter t ~f =
  let rec loop = function
  | None -> ()
  | Some el -> f (value el); loop (next el)
  in
  loop !t

let find_el t ~f =
  let rec loop = function
  | None -> None
  | Some elt ->
    if f (value elt) then Some elt
    else loop (next elt)
  in
  loop !t

  let new_created_list filepath list =
    let outro = Out_channel.create filepath in
    List.iter list ~f:(fun  -> fprintf outro "%d\n" x);
    Out_channel.close outro

(* List.iter bny_data ~f:(fun x -> Core.Std.printf "%s\n%!" x) 
* 
* let first_elem = List.hd db_data in 
* match first_elem with 
* | None -> Core.Std.printf "this is an error" 
* | Some e -> Core.Std.printf "Hi %s\n%!" e 
* 
* 
* let all_elems = List.nth db_data_listify 23 in 
* match all_elems with 
* | None -> Core.Std.printf "this is an error" 
* | Some e -> Core.Std.printf "Hi %s\n%!" e *)

let command =
  Command.basic
    ~summary:"parse depo file"
    Command.Spec.(
      empty
    )
    (fun () -> main()
    )
    
let () = Command.run command