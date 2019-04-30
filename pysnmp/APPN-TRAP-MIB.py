#
# PySNMP MIB module APPN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPN-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:08:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
dlurDlusSessnStatus, = mibBuilder.importSymbols("APPN-DLUR-MIB", "dlurDlusSessnStatus")
appnLsOperState, appnPortOperState, appnIsInP2SFmdPius, appnMIB, appnIsInP2SNonFmdPius, appnIsInP2SFmdBytes, appnIsInS2PFmdPius, appnIsInP2SNonFmdBytes, appnIsInS2PNonFmdBytes, appnIsInS2PFmdBytes, appnLocalTgOperational, appnLocalTgCpCpSession, appnIsInS2PNonFmdPius, appnGroups, appnObjects, appnIsInSessUpTime, appnCompliances = mibBuilder.importSymbols("APPN-MIB", "appnLsOperState", "appnPortOperState", "appnIsInP2SFmdPius", "appnMIB", "appnIsInP2SNonFmdPius", "appnIsInP2SFmdBytes", "appnIsInS2PFmdPius", "appnIsInP2SNonFmdBytes", "appnIsInS2PNonFmdBytes", "appnIsInS2PFmdBytes", "appnLocalTgOperational", "appnLocalTgCpCpSession", "appnIsInS2PNonFmdPius", "appnGroups", "appnObjects", "appnIsInSessUpTime", "appnCompliances")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, IpAddress, Bits, ObjectIdentity, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, iso, Integer32, Counter32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "iso", "Integer32", "Counter32", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
appnTrapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 4, 0))
if mibBuilder.loadTexts: appnTrapMIB.setLastUpdated('9808310000Z')
if mibBuilder.loadTexts: appnTrapMIB.setOrganization('IETF SNA NAU MIB WG / AIW APPN MIBs SIG')
appnIsrAccountingDataTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 1)).setObjects(("APPN-MIB", "appnIsInP2SFmdPius"), ("APPN-MIB", "appnIsInS2PFmdPius"), ("APPN-MIB", "appnIsInP2SNonFmdPius"), ("APPN-MIB", "appnIsInS2PNonFmdPius"), ("APPN-MIB", "appnIsInP2SFmdBytes"), ("APPN-MIB", "appnIsInS2PFmdBytes"), ("APPN-MIB", "appnIsInP2SNonFmdBytes"), ("APPN-MIB", "appnIsInS2PNonFmdBytes"), ("APPN-MIB", "appnIsInSessUpTime"))
if mibBuilder.loadTexts: appnIsrAccountingDataTrap.setStatus('current')
appnLocalTgOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 2)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgOperational"))
if mibBuilder.loadTexts: appnLocalTgOperStateChangeTrap.setStatus('current')
appnLocalTgCpCpChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 3)).setObjects(("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-MIB", "appnLocalTgCpCpSession"))
if mibBuilder.loadTexts: appnLocalTgCpCpChangeTrap.setStatus('current')
appnPortOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 4)).setObjects(("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-MIB", "appnPortOperState"))
if mibBuilder.loadTexts: appnPortOperStateChangeTrap.setStatus('current')
appnLsOperStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 5)).setObjects(("APPN-TRAP-MIB", "appnLsTableChanges"), ("APPN-MIB", "appnLsOperState"))
if mibBuilder.loadTexts: appnLsOperStateChangeTrap.setStatus('current')
dlurDlusStateChangeTrap = NotificationType((1, 3, 6, 1, 2, 1, 34, 4, 0, 6)).setObjects(("APPN-TRAP-MIB", "dlurDlusTableChanges"), ("APPN-DLUR-MIB", "dlurDlusSessnStatus"))
if mibBuilder.loadTexts: dlurDlusStateChangeTrap.setStatus('current')
appnTrapObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 34, 4, 1, 7))
appnTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 1), Bits().clone(namedValues=NamedValues(("appnLocalTgOperStateChangeTrap", 0), ("appnLocalTgCpCpChangeTrap", 1), ("appnPortOperStateChangeTrap", 2), ("appnLsOperStateChangeTrap", 3), ("dlurDlusStateChangeTrap", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: appnTrapControl.setStatus('current')
appnLocalTgTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLocalTgTableChanges.setStatus('current')
appnPortTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnPortTableChanges.setStatus('current')
appnLsTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appnLsTableChanges.setStatus('current')
dlurDlusTableChanges = MibScalar((1, 3, 6, 1, 2, 1, 34, 4, 1, 7, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dlurDlusTableChanges.setStatus('current')
appnTrapMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 4, 3, 1, 2)).setObjects(("APPN-TRAP-MIB", "appnTrapMibIsrNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibTopoNotifGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurConfGroup"), ("APPN-TRAP-MIB", "appnTrapMibDlurNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibCompliance = appnTrapMibCompliance.setStatus('current')
appnTrapMibIsrNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 21)).setObjects(("APPN-TRAP-MIB", "appnIsrAccountingDataTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibIsrNotifGroup = appnTrapMibIsrNotifGroup.setStatus('current')
appnTrapMibTopoConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 22)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "appnLocalTgTableChanges"), ("APPN-TRAP-MIB", "appnPortTableChanges"), ("APPN-TRAP-MIB", "appnLsTableChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibTopoConfGroup = appnTrapMibTopoConfGroup.setStatus('current')
appnTrapMibTopoNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 23)).setObjects(("APPN-TRAP-MIB", "appnLocalTgOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLocalTgCpCpChangeTrap"), ("APPN-TRAP-MIB", "appnPortOperStateChangeTrap"), ("APPN-TRAP-MIB", "appnLsOperStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibTopoNotifGroup = appnTrapMibTopoNotifGroup.setStatus('current')
appnTrapMibDlurConfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 24)).setObjects(("APPN-TRAP-MIB", "appnTrapControl"), ("APPN-TRAP-MIB", "dlurDlusTableChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibDlurConfGroup = appnTrapMibDlurConfGroup.setStatus('current')
appnTrapMibDlurNotifGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 34, 4, 3, 2, 25)).setObjects(("APPN-TRAP-MIB", "dlurDlusStateChangeTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    appnTrapMibDlurNotifGroup = appnTrapMibDlurNotifGroup.setStatus('current')
mibBuilder.exportSymbols("APPN-TRAP-MIB", appnTrapObjects=appnTrapObjects, appnTrapMIB=appnTrapMIB, dlurDlusTableChanges=dlurDlusTableChanges, appnPortOperStateChangeTrap=appnPortOperStateChangeTrap, appnIsrAccountingDataTrap=appnIsrAccountingDataTrap, appnPortTableChanges=appnPortTableChanges, dlurDlusStateChangeTrap=dlurDlusStateChangeTrap, appnLocalTgCpCpChangeTrap=appnLocalTgCpCpChangeTrap, PYSNMP_MODULE_ID=appnTrapMIB, appnTrapMibCompliance=appnTrapMibCompliance, appnLsTableChanges=appnLsTableChanges, appnTrapMibTopoConfGroup=appnTrapMibTopoConfGroup, appnLsOperStateChangeTrap=appnLsOperStateChangeTrap, appnLocalTgOperStateChangeTrap=appnLocalTgOperStateChangeTrap, appnTrapMibIsrNotifGroup=appnTrapMibIsrNotifGroup, appnTrapMibTopoNotifGroup=appnTrapMibTopoNotifGroup, appnTrapMibDlurNotifGroup=appnTrapMibDlurNotifGroup, appnLocalTgTableChanges=appnLocalTgTableChanges, appnTrapMibDlurConfGroup=appnTrapMibDlurConfGroup, appnTrapControl=appnTrapControl)
