#
# PySNMP MIB module CISCO-DMN-DSG-FPUI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-FPUI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Bits, TimeTicks, Integer32, Counter64, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, NotificationType, Unsigned32, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "NotificationType", "Unsigned32", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGFPUI = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24))
ciscoDSGFPUI.setRevisions(('2010-08-30 11:00', '2010-03-22 05:00', '2009-12-20 12:00',))
if mibBuilder.loadTexts: ciscoDSGFPUI.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGFPUI.setOrganization('Cisco Systems, Inc.')
fpuiKBLock = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiKBLock.setStatus('current')
fpuiKBLockTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiKBLockTimeout.setStatus('current')
fpuiLCDContrast = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiLCDContrast.setStatus('current')
fpuiAWReminder = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiAWReminder.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-FPUI-MIB", ciscoDSGFPUI=ciscoDSGFPUI, fpuiKBLockTimeout=fpuiKBLockTimeout, PYSNMP_MODULE_ID=ciscoDSGFPUI, fpuiAWReminder=fpuiAWReminder, fpuiLCDContrast=fpuiLCDContrast, fpuiKBLock=fpuiKBLock)
