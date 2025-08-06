import java.util.*;

public class col
{
    public static void main(String[] args){
        ArrayList<Integer> ls = new ArrayList<>();
        ls.add(7);
        ls.add(9);
        ls.add(4);
        ls.add(12);
        ls.add(3);
        System.out.println(ls);
        System.out.println(ls.get(3));
        System.out.println(ls.size());
        System.out.println(ls.set(3,23));
        System.out.println(ls.remove(4));
        for (int i = 0; i < ls.size() - 1; i++){
            int maxIdx = i;
            for  (int j = i+1; j <ls.size() ; j++){
                if(ls.get(j) > ls.get(maxIdx)){
                    maxIdx = j;
                }
            }
            int temp = ls.get(i);
            ls.set(i, ls.get(maxIdx));
            ls.set(maxIdx, temp);
        }
        System.out.println(ls);
    }        
}
