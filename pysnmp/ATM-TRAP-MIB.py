#
# PySNMP MIB module ATM-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
atmPortCardIndex, atmPortPortIndex, atmPortSscopStatus = mibBuilder.importSymbols("CENTILLION-ATMCFG-MIB", "atmPortCardIndex", "atmPortPortIndex", "atmPortSscopStatus")
atmTraps, = mibBuilder.importSymbols("S5-ROOT-MIB", "atmTraps")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Bits, TimeTicks, Counter64, Integer32, ModuleIdentity, NotificationType, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Bits", "TimeTicks", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
s5CtrSscopDown = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7) + (0,1)).setObjects(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"), ("CENTILLION-ATMCFG-MIB", "atmPortPortIndex"), ("CENTILLION-ATMCFG-MIB", "atmPortSscopStatus"))
s5CtrAdmaLockup = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7) + (0,2)).setObjects(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"), ("CENTILLION-ATMCFG-MIB", "atmPortPortIndex"))
s5CtrAcmaLockup = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7) + (0,3)).setObjects(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"))
mibBuilder.exportSymbols("ATM-TRAP-MIB", s5CtrAdmaLockup=s5CtrAdmaLockup, s5CtrAcmaLockup=s5CtrAcmaLockup, s5CtrSscopDown=s5CtrSscopDown)
