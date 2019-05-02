#
# PySNMP MIB module CISCO-IETF-PIM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PIM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, MibIdentifier, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, NotificationType, Unsigned32, Counter64, iso, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibIdentifier", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "NotificationType", "Unsigned32", "Counter64", "iso", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfPimCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 441))
ciscoIetfPimCapability.setRevisions(('2005-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfPimCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfPimCapability.setLastUpdated('200507270000Z')
if mibBuilder.loadTexts: ciscoIetfPimCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfPimCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoIetfPimCapability.setDescription('The capabilities description of CISCO-IETF-PIM-MIB')
cIetfPimCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 441, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimCapV320CRS1 = cIetfPimCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimCapV320CRS1 = cIetfPimCapV320CRS1.setStatus('current')
if mibBuilder.loadTexts: cIetfPimCapV320CRS1.setDescription('CISCO-IETF-PIM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-PIM-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfPimCapability, cIetfPimCapV320CRS1=cIetfPimCapV320CRS1, ciscoIetfPimCapability=ciscoIetfPimCapability)
