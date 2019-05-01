#
# PySNMP MIB module DES3810-52-SWITCH-RESOURCE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DES3810-52-SWITCH-RESOURCE-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:41:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, ModuleIdentity, Counter64, TimeTicks, Unsigned32, MibIdentifier, Bits, ObjectIdentity, iso, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "ModuleIdentity", "Counter64", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "ObjectIdentity", "iso", "Counter32", "IpAddress")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
des3810_52, = mibBuilder.importSymbols("SW3810PRIMGMT-MIB", "des3810-52")
swSwitchResourceMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4))
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setLastUpdated('201005060000Z')
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setDescription('The Structure of switch resource management for the proprietary enterprise.')
swSwitchResourceMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1))
swSwitchResourceMgmtSRMMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("vpws", 2))).clone('routing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMMode.setStatus('current')
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMMode.setDescription('The switch configure SRM mode, it need be saved and will be taken effect after reboot.')
swSwitchResourceMgmtSRMCurrentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("vpws", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMCurrentMode.setStatus('current')
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMCurrentMode.setDescription('The switch current SRM mode.')
mibBuilder.exportSymbols("DES3810-52-SWITCH-RESOURCE-MGMT-MIB", PYSNMP_MODULE_ID=swSwitchResourceMgmtMIB, swSwitchResourceMgmtSRMCurrentMode=swSwitchResourceMgmtSRMCurrentMode, swSwitchResourceMgmtMIB=swSwitchResourceMgmtMIB, swSwitchResourceMgmtMIBObjects=swSwitchResourceMgmtMIBObjects, swSwitchResourceMgmtSRMMode=swSwitchResourceMgmtSRMMode)
