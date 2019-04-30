#
# PySNMP MIB module Fore-Ima-Ext-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Ima-Ext-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
asx, atmSwitch = mibBuilder.importSymbols("Fore-Common-MIB", "asx", "atmSwitch")
imaGroupIndex, = mibBuilder.importSymbols("IMA-MIB", "imaGroupIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, iso, IpAddress, Gauge32, ObjectIdentity, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "iso", "IpAddress", "Gauge32", "ObjectIdentity", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreImaExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19))
if mibBuilder.loadTexts: foreImaExtMib.setLastUpdated('0005110000Z')
if mibBuilder.loadTexts: foreImaExtMib.setOrganization('Marconi')
foreImaVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1))
class ForeImaVersionNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("v10", 1), ("v11", 2))

foreImaVersionTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1), )
if mibBuilder.loadTexts: foreImaVersionTable.setStatus('current')
foreImaVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1), ).setIndexNames((0, "IMA-MIB", "imaGroupIndex"))
if mibBuilder.loadTexts: foreImaVersionEntry.setStatus('current')
foreImaVersionConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1, 1), ForeImaVersionNumber().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: foreImaVersionConfigured.setStatus('current')
foreImaVersionOperational = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1, 2), ForeImaVersionNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: foreImaVersionOperational.setStatus('current')
mibBuilder.exportSymbols("Fore-Ima-Ext-MIB", ForeImaVersionNumber=ForeImaVersionNumber, foreImaExtMib=foreImaExtMib, foreImaVersion=foreImaVersion, foreImaVersionTable=foreImaVersionTable, foreImaVersionOperational=foreImaVersionOperational, PYSNMP_MODULE_ID=foreImaExtMib, foreImaVersionEntry=foreImaVersionEntry, foreImaVersionConfigured=foreImaVersionConfigured)
