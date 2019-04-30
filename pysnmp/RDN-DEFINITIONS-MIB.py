#
# PySNMP MIB module RDN-DEFINITIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-DEFINITIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
riverdelta, = mibBuilder.importSymbols("RDN-MIB", "riverdelta")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter64, IpAddress, Counter32, MibIdentifier, Integer32, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter64", "IpAddress", "Counter32", "MibIdentifier", "Integer32", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rdnDefinitions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4))
rdnDefinitions.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2002-12-10 00:00', '2001-04-18 00:00',))
if mibBuilder.loadTexts: rdnDefinitions.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnDefinitions.setOrganization('Motorola')
mibBuilder.exportSymbols("RDN-DEFINITIONS-MIB", PYSNMP_MODULE_ID=rdnDefinitions, rdnDefinitions=rdnDefinitions)
