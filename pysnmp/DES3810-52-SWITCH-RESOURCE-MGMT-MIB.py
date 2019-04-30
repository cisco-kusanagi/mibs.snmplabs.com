#
# PySNMP MIB module DES3810-52-SWITCH-RESOURCE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DES3810-52-SWITCH-RESOURCE-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, MibIdentifier, Integer32, Gauge32, NotificationType, iso, IpAddress, Bits, TimeTicks, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "MibIdentifier", "Integer32", "Gauge32", "NotificationType", "iso", "IpAddress", "Bits", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
des3810_52, = mibBuilder.importSymbols("SW3810PRIMGMT-MIB", "des3810-52")
swSwitchResourceMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4))
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setLastUpdated('201005060000Z')
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setOrganization('D-Link Corp.')
swSwitchResourceMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1))
swSwitchResourceMgmtSRMMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("vpws", 2))).clone('routing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMMode.setStatus('current')
swSwitchResourceMgmtSRMCurrentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("vpws", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMCurrentMode.setStatus('current')
mibBuilder.exportSymbols("DES3810-52-SWITCH-RESOURCE-MGMT-MIB", PYSNMP_MODULE_ID=swSwitchResourceMgmtMIB, swSwitchResourceMgmtMIBObjects=swSwitchResourceMgmtMIBObjects, swSwitchResourceMgmtMIB=swSwitchResourceMgmtMIB, swSwitchResourceMgmtSRMMode=swSwitchResourceMgmtSRMMode, swSwitchResourceMgmtSRMCurrentMode=swSwitchResourceMgmtSRMCurrentMode)
