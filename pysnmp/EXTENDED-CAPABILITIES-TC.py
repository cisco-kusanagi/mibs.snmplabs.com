#
# PySNMP MIB module EXTENDED-CAPABILITIES-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTENDED-CAPABILITIES-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, Bits, iso, Gauge32, IpAddress, MibIdentifier, enterprises, ObjectIdentity, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Bits", "iso", "Gauge32", "IpAddress", "MibIdentifier", "enterprises", "ObjectIdentity", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
extendedCapabilitiesList = ModuleIdentity((1, 3, 6, 1, 4, 1, 1579, 42, 1, 3, 1))
if mibBuilder.loadTexts: extendedCapabilitiesList.setLastUpdated('200208170000Z')
if mibBuilder.loadTexts: extendedCapabilitiesList.setOrganization('University of Liverpool')
class ExtendedCapabilities(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("oidDeltaCompression", 0), ("oidPrefixCompression", 1), ("fillHolesInTables", 2), ("dontColumnWrap", 3), ("errorString", 4))

mibBuilder.exportSymbols("EXTENDED-CAPABILITIES-TC", extendedCapabilitiesList=extendedCapabilitiesList, PYSNMP_MODULE_ID=extendedCapabilitiesList, ExtendedCapabilities=ExtendedCapabilities)
