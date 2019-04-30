#
# PySNMP MIB module CXPortManager-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXPortManager-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cxPortManager, = mibBuilder.importSymbols("CXProduct-SMI", "cxPortManager")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Integer32, ObjectIdentity, IpAddress, NotificationType, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Gauge32, ModuleIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "ObjectIdentity", "IpAddress", "NotificationType", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxPrtMPlannedCfgTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 1), )
if mibBuilder.loadTexts: cxPrtMPlannedCfgTable.setStatus('mandatory')
cxPrtMPlannedCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 1, 1), ).setIndexNames((0, "CXPortManager-MIB", "cxPrtMPrtNum"))
if mibBuilder.loadTexts: cxPrtMPlannedCfgEntry.setStatus('mandatory')
cxPrtMPrtNum = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxPrtMPrtNum.setStatus('mandatory')
cxPrtMPrtType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxPrtMPrtType.setStatus('mandatory')
cxPrtMAdminTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 2), )
if mibBuilder.loadTexts: cxPrtMAdminTable.setStatus('mandatory')
cxPrtMAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 2, 1), ).setIndexNames((0, "CXPortManager-MIB", "cxPrtMPrtNum"))
if mibBuilder.loadTexts: cxPrtMAdminEntry.setStatus('mandatory')
cxPrtMAdminPortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("activate", 1), ("deactivate", 2), ("reinitialize", 3)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cxPrtMAdminPortControl.setStatus('mandatory')
mibBuilder.exportSymbols("CXPortManager-MIB", cxPrtMPlannedCfgTable=cxPrtMPlannedCfgTable, cxPrtMPrtType=cxPrtMPrtType, cxPrtMPlannedCfgEntry=cxPrtMPlannedCfgEntry, cxPrtMPrtNum=cxPrtMPrtNum, cxPrtMAdminTable=cxPrtMAdminTable, cxPrtMAdminEntry=cxPrtMAdminEntry, cxPrtMAdminPortControl=cxPrtMAdminPortControl)
