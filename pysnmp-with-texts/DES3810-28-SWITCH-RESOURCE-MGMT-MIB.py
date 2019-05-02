#
# PySNMP MIB module DES3810-28-SWITCH-RESOURCE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DES3810-28-SWITCH-RESOURCE-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:41:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, MibIdentifier, Gauge32, Counter64, NotificationType, TimeTicks, Counter32, Bits, Integer32, IpAddress, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibIdentifier", "Gauge32", "Counter64", "NotificationType", "TimeTicks", "Counter32", "Bits", "Integer32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
des3810_28, = mibBuilder.importSymbols("SW3810PRIMGMT-MIB", "des3810-28")
swSwitchResourceMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1, 4))
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setLastUpdated('201005060000Z')
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setDescription('The Structure of switch resource management for the proprietary enterprise.')
swSwitchResourceMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1, 4, 1))
swSwitchResourceMgmtSRMMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("vpws", 2))).clone('routing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMMode.setStatus('current')
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMMode.setDescription('The switch configure SRM mode, it need be saved and will be taken effect after reboot.')
swSwitchResourceMgmtSRMCurrentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("vpws", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMCurrentMode.setStatus('current')
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMCurrentMode.setDescription('The switch current SRM mode.')
mibBuilder.exportSymbols("DES3810-28-SWITCH-RESOURCE-MGMT-MIB", swSwitchResourceMgmtMIBObjects=swSwitchResourceMgmtMIBObjects, swSwitchResourceMgmtMIB=swSwitchResourceMgmtMIB, PYSNMP_MODULE_ID=swSwitchResourceMgmtMIB, swSwitchResourceMgmtSRMCurrentMode=swSwitchResourceMgmtSRMCurrentMode, swSwitchResourceMgmtSRMMode=swSwitchResourceMgmtSRMMode)
