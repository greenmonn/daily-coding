import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class ErrorTest0 {

    public static boolean debug = false;

    @Test
    public void test1() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "ErrorTest0.test1");
        Account account1 = new Account((int) (short) 0);
        boolean boolean3 = account1.Borrow((int) '4');
        boolean boolean5 = account1.Borrow((int) '4');
        boolean boolean7 = account1.Borrow((int) (short) 100);
        boolean boolean9 = account1.Borrow((int) (short) 100);
    }

    @Test
    public void test2() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "ErrorTest0.test2");
        Account account1 = new Account((-1));
        boolean boolean3 = account1.Receive((int) (short) 1);
        boolean boolean5 = account1.Repay((int) (short) -1);
        boolean boolean7 = account1.Borrow((int) 'a');
        boolean boolean9 = account1.Receive((int) (short) 0);
        boolean boolean11 = account1.Borrow((int) (short) 100);
        boolean boolean13 = account1.Borrow((int) '4');
        boolean boolean15 = account1.Borrow((int) '4');
    }

    @Test
    public void test3() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "ErrorTest0.test3");
        Account account1 = new Account((int) 'a');
        boolean boolean3 = account1.Borrow((int) '#');
        boolean boolean5 = account1.Repay((int) '#');
        boolean boolean7 = account1.Borrow((int) (short) 10);
        java.lang.Class<?> wildcardClass8 = account1.getClass();
        boolean boolean10 = account1.Borrow((int) '4');
        boolean boolean12 = account1.Borrow((int) '4');
        boolean boolean14 = account1.Borrow(100);
        boolean boolean16 = account1.Borrow((int) (byte) 100);
    }

    @Test
    public void test4() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "ErrorTest0.test4");
        Account account1 = new Account((int) 'a');
        boolean boolean3 = account1.Borrow((int) '#');
        boolean boolean5 = account1.Repay((int) '#');
        boolean boolean7 = account1.Borrow((int) (short) 10);
        java.lang.Class<?> wildcardClass8 = account1.getClass();
        boolean boolean10 = account1.Borrow((int) '4');
        boolean boolean12 = account1.Send(0);
        java.lang.Class<?> wildcardClass13 = account1.getClass();
        boolean boolean15 = account1.Receive(0);
        boolean boolean17 = account1.Borrow((int) '4');
        boolean boolean19 = account1.Borrow(1);
        boolean boolean21 = account1.Borrow(100);
        boolean boolean23 = account1.Borrow((int) (short) 100);
    }

    @Test
    public void test5() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "ErrorTest0.test5");
        Account account1 = new Account((int) (short) 0);
        boolean boolean3 = account1.Borrow((int) '4');
        boolean boolean5 = account1.Borrow((int) '4');
        boolean boolean7 = account1.Borrow((int) (short) 100);
        java.lang.Class<?> wildcardClass8 = account1.getClass();
        boolean boolean10 = account1.Borrow((int) (byte) 100);
    }

    @Test
    public void test6() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "ErrorTest0.test6");
        Account account1 = new Account((int) (byte) 1);
        boolean boolean3 = account1.Send((int) (byte) 100);
        boolean boolean5 = account1.Repay(0);
        boolean boolean7 = account1.Borrow(1);
        boolean boolean9 = account1.Receive((int) (short) 1);
        boolean boolean11 = account1.Borrow(100);
        boolean boolean13 = account1.Receive((int) (byte) -1);
        boolean boolean15 = account1.Borrow(100);
    }

    @Test
    public void test7() throws Throwable {
        if (debug)
            System.out.format("%n%s%n", "ErrorTest0.test7");
        Account account1 = new Account((int) (short) 0);
        boolean boolean3 = account1.Borrow((int) '4');
        boolean boolean5 = account1.Borrow((int) '4');
        boolean boolean7 = account1.Borrow((int) (short) 100);
        boolean boolean9 = account1.Send((int) (short) 0);
        boolean boolean11 = account1.Borrow((int) (byte) 100);
    }
}

