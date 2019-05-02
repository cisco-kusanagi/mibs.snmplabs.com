#
# PySNMP MIB module Fore-Ima-Ext-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Ima-Ext-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
atmSwitch, asx = mibBuilder.importSymbols("Fore-Common-MIB", "atmSwitch", "asx")
imaGroupIndex, = mibBuilder.importSymbols("IMA-MIB", "imaGroupIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Counter32, iso, Counter64, TimeTicks, ModuleIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter32", "iso", "Counter64", "TimeTicks", "ModuleIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreImaExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19))
if mibBuilder.loadTexts: foreImaExtMib.setLastUpdated('0005110000Z')
if mibBuilder.loadTexts: foreImaExtMib.setOrganization('Marconi')
if mibBuilder.loadTexts: foreImaExtMib.setContactInfo(' Postal: Marconi 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: foreImaExtMib.setDescription(' This MIB defines extensions to the standard ATM-FORUM IMA MIB to facilitate extended IMA configurations supported by Marconi.')
foreImaVersion = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1))
class ForeImaVersionNumber(TextualConvention, Integer32):
    description = 'This variable represents the ATM-FORUM IMA Version number. The possible values are v10 (1) and v11 (2).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("v10", 1), ("v11", 2))

foreImaVersionTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1), )
if mibBuilder.loadTexts: foreImaVersionTable.setStatus('current')
if mibBuilder.loadTexts: foreImaVersionTable.setDescription('A table of IMA Group ifIndeces with their associated IMA version.')
foreImaVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1), ).setIndexNames((0, "IMA-MIB", "imaGroupIndex"))
if mibBuilder.loadTexts: foreImaVersionEntry.setStatus('current')
if mibBuilder.loadTexts: foreImaVersionEntry.setDescription('A table entry listing the association of IMA group index and IMA version.')
foreImaVersionConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1, 1), ForeImaVersionNumber().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: foreImaVersionConfigured.setStatus('current')
if mibBuilder.loadTexts: foreImaVersionConfigured.setDescription('Configured IMA version of IMA group')
foreImaVersionOperational = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 19, 1, 1, 1, 2), ForeImaVersionNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: foreImaVersionOperational.setStatus('current')
if mibBuilder.loadTexts: foreImaVersionOperational.setDescription('Operational IMA version of IMA group')
mibBuilder.exportSymbols("Fore-Ima-Ext-MIB", PYSNMP_MODULE_ID=foreImaExtMib, foreImaVersion=foreImaVersion, foreImaVersionEntry=foreImaVersionEntry, foreImaVersionConfigured=foreImaVersionConfigured, foreImaVersionTable=foreImaVersionTable, foreImaExtMib=foreImaExtMib, foreImaVersionOperational=foreImaVersionOperational, ForeImaVersionNumber=ForeImaVersionNumber)
