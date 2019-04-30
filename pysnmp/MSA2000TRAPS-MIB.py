#
# PySNMP MIB module MSA2000TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSA2000TRAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
connUnitEventType, connUnitEventDescr, connUnitEventId = mibBuilder.importSymbols("FCMGMT-MIB", "connUnitEventType", "connUnitEventDescr", "connUnitEventId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, enterprises, Gauge32, ModuleIdentity, Integer32, Unsigned32, TimeTicks, Bits, ObjectIdentity, iso, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "enterprises", "Gauge32", "ModuleIdentity", "Integer32", "Unsigned32", "TimeTicks", "Bits", "ObjectIdentity", "iso", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
hpMSA = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 51))
mibName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 51, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mibName.setStatus('mandatory')
msaEventInfoTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3001)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
msaEventWarningTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3002)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
msaEventErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3003)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
msaEventCriticalTrap = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 51) + (0,3004)).setObjects(("FCMGMT-MIB", "connUnitEventId"), ("FCMGMT-MIB", "connUnitEventType"), ("FCMGMT-MIB", "connUnitEventDescr"))
mibBuilder.exportSymbols("MSA2000TRAPS-MIB", msaEventInfoTrap=msaEventInfoTrap, hpMSA=hpMSA, msaEventErrorTrap=msaEventErrorTrap, nm=nm, mibName=mibName, hp=hp, msaEventWarningTrap=msaEventWarningTrap, msaEventCriticalTrap=msaEventCriticalTrap)
