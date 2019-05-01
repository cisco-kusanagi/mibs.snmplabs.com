#
# PySNMP MIB module CISCO-IETF-PIM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PIM-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, Counter32, TimeTicks, IpAddress, iso, NotificationType, ObjectIdentity, MibIdentifier, Unsigned32, Integer32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "TimeTicks", "IpAddress", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Integer32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfPimExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 443))
ciscoIetfPimExtCapability.setRevisions(('2005-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setLastUpdated('200507270000Z')
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setDescription('The capabilities description of CISCO-IETF-PIM-EXT-MIB')
cIetfPimExtCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 443, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimExtCapV320CRS1 = cIetfPimExtCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimExtCapV320CRS1 = cIetfPimExtCapV320CRS1.setStatus('current')
if mibBuilder.loadTexts: cIetfPimExtCapV320CRS1.setDescription('CISCO-IETF-PIM-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-PIM-EXT-CAPABILITY", cIetfPimExtCapV320CRS1=cIetfPimExtCapV320CRS1, ciscoIetfPimExtCapability=ciscoIetfPimExtCapability, PYSNMP_MODULE_ID=ciscoIetfPimExtCapability)
