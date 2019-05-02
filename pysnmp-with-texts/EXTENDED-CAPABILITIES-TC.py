#
# PySNMP MIB module EXTENDED-CAPABILITIES-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTENDED-CAPABILITIES-TC
# Produced by pysmi-0.3.4 at Wed May  1 13:07:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, enterprises, ObjectIdentity, TimeTicks, Gauge32, Bits, Unsigned32, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "enterprises", "ObjectIdentity", "TimeTicks", "Gauge32", "Bits", "Unsigned32", "Counter32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extendedCapabilitiesList = ModuleIdentity((1, 3, 6, 1, 4, 1, 1579, 42, 1, 3, 1))
if mibBuilder.loadTexts: extendedCapabilitiesList.setLastUpdated('200208170000Z')
if mibBuilder.loadTexts: extendedCapabilitiesList.setOrganization('University of Liverpool')
if mibBuilder.loadTexts: extendedCapabilitiesList.setContactInfo('Postal: Dave Shield Computer Science University of Liverpool Peach Street Liverpool L69 7ZF United Kingdom E-Mail: D.T.Shield@csc.liv.ac.uk')
if mibBuilder.loadTexts: extendedCapabilitiesList.setDescription('This MIB module defines a provisional textual convention for identifying extended SNMP capabilities.')
class ExtendedCapabilities(TextualConvention, Bits):
    description = 'Provisional list of extended SNMP capabilities.'
    status = 'current'
    namedValues = NamedValues(("oidDeltaCompression", 0), ("oidPrefixCompression", 1), ("fillHolesInTables", 2), ("dontColumnWrap", 3), ("errorString", 4))

mibBuilder.exportSymbols("EXTENDED-CAPABILITIES-TC", extendedCapabilitiesList=extendedCapabilitiesList, ExtendedCapabilities=ExtendedCapabilities, PYSNMP_MODULE_ID=extendedCapabilitiesList)
