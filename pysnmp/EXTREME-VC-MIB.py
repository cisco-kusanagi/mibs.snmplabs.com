#
# PySNMP MIB module EXTREME-VC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:53:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, Counter64, Counter32, NotificationType, Integer32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "Integer32", "IpAddress", "TimeTicks")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
extremeVC = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 5))
if mibBuilder.loadTexts: extremeVC.setLastUpdated('9801090000Z')
if mibBuilder.loadTexts: extremeVC.setOrganization('Extreme Networks, Inc.')
extremeVCLinkTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1), )
if mibBuilder.loadTexts: extremeVCLinkTable.setStatus('deprecated')
extremeVCLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extremeVCLinkEntry.setStatus('deprecated')
extremeVCLinkValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVCLinkValid.setStatus('deprecated')
extremeVCLinkDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVCLinkDeviceId.setStatus('deprecated')
extremeVCLinkPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVCLinkPortIndex.setStatus('deprecated')
mibBuilder.exportSymbols("EXTREME-VC-MIB", extremeVC=extremeVC, extremeVCLinkEntry=extremeVCLinkEntry, extremeVCLinkPortIndex=extremeVCLinkPortIndex, extremeVCLinkValid=extremeVCLinkValid, extremeVCLinkDeviceId=extremeVCLinkDeviceId, PYSNMP_MODULE_ID=extremeVC, extremeVCLinkTable=extremeVCLinkTable)
