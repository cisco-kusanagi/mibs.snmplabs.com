#
# PySNMP MIB module CISCO-DMN-DSG-FPUI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-FPUI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, ObjectIdentity, ModuleIdentity, Bits, Integer32, Gauge32, NotificationType, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Bits", "Integer32", "Gauge32", "NotificationType", "Counter64", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGFPUI = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24))
ciscoDSGFPUI.setRevisions(('2010-08-30 11:00', '2010-03-22 05:00', '2009-12-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGFPUI.setRevisionsDescriptions(('V01.00.02 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.01 2010-03-22 The Syntax of Unsigned32 MIB objects whose range is within the range of Integer32, is updated to Integer32.', 'V01.00.00 2009-12-20 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGFPUI.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGFPUI.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGFPUI.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGFPUI.setDescription('Cisco Front Panel User Interface MIB.')
fpuiKBLock = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiKBLock.setStatus('current')
if mibBuilder.loadTexts: fpuiKBLock.setDescription('Controls the keyboard lock.')
fpuiKBLockTimeout = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1800))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiKBLockTimeout.setStatus('current')
if mibBuilder.loadTexts: fpuiKBLockTimeout.setDescription('Keyboard lock timeout.')
fpuiLCDContrast = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiLCDContrast.setStatus('current')
if mibBuilder.loadTexts: fpuiLCDContrast.setDescription('LCD contrast setting.')
fpuiAWReminder = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 24, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fpuiAWReminder.setStatus('current')
if mibBuilder.loadTexts: fpuiAWReminder.setDescription('Enable/Disable flashing alarms and warnings on front panel.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-FPUI-MIB", fpuiAWReminder=fpuiAWReminder, ciscoDSGFPUI=ciscoDSGFPUI, fpuiLCDContrast=fpuiLCDContrast, fpuiKBLockTimeout=fpuiKBLockTimeout, PYSNMP_MODULE_ID=ciscoDSGFPUI, fpuiKBLock=fpuiKBLock)
