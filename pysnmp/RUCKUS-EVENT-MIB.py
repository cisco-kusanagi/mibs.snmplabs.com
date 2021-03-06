#
# PySNMP MIB module RUCKUS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ruckusEvents, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusEvents")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, MibIdentifier, IpAddress, ModuleIdentity, Unsigned32, ObjectIdentity, Gauge32, Counter32, Counter64, Bits, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "MibIdentifier", "IpAddress", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter32", "Counter64", "Bits", "iso", "NotificationType")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
ruckusEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 2, 1))
if mibBuilder.loadTexts: ruckusEventMIB.setLastUpdated('201010150000Z')
if mibBuilder.loadTexts: ruckusEventMIB.setOrganization('Ruckus Wireless, Inc.')
ruckusEventTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1))
ruckusEventObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 2, 1, 2))
ruckusEventAssocTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 1)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr"))
if mibBuilder.loadTexts: ruckusEventAssocTrap.setStatus('current')
ruckusEventDiassocTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 2)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr"))
if mibBuilder.loadTexts: ruckusEventDiassocTrap.setStatus('current')
ruckusEventSetErrorTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 3)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventSetErrorOID"))
if mibBuilder.loadTexts: ruckusEventSetErrorTrap.setStatus('current')
ruckusEventConnectTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 25)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr"))
if mibBuilder.loadTexts: ruckusEventConnectTrap.setStatus('current')
ruckusEventDisconnectTrap = NotificationType((1, 3, 6, 1, 4, 1, 25053, 2, 1, 1, 26)).setObjects(("RUCKUS-EVENT-MIB", "ruckusEventClientMacAddr"))
if mibBuilder.loadTexts: ruckusEventDisconnectTrap.setStatus('current')
ruckusEventClientMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 2, 1, 2, 15), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ruckusEventClientMacAddr.setStatus('current')
ruckusEventSetErrorOID = MibScalar((1, 3, 6, 1, 4, 1, 25053, 2, 1, 2, 20), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ruckusEventSetErrorOID.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-EVENT-MIB", ruckusEventDiassocTrap=ruckusEventDiassocTrap, ruckusEventTraps=ruckusEventTraps, ruckusEventSetErrorOID=ruckusEventSetErrorOID, PYSNMP_MODULE_ID=ruckusEventMIB, ruckusEventSetErrorTrap=ruckusEventSetErrorTrap, ruckusEventClientMacAddr=ruckusEventClientMacAddr, ruckusEventDisconnectTrap=ruckusEventDisconnectTrap, ruckusEventMIB=ruckusEventMIB, ruckusEventObjects=ruckusEventObjects, ruckusEventAssocTrap=ruckusEventAssocTrap, ruckusEventConnectTrap=ruckusEventConnectTrap)
