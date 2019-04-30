#
# PySNMP MIB module CISCO-IETF-PIM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PIM-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, Integer32, TimeTicks, IpAddress, MibIdentifier, NotificationType, Gauge32, Bits, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "TimeTicks", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "Bits", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfPimExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 443))
ciscoIetfPimExtCapability.setRevisions(('2005-07-27 00:00',))
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setLastUpdated('200507270000Z')
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setOrganization('Cisco Systems, Inc.')
cIetfPimExtCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 443, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimExtCapV320CRS1 = cIetfPimExtCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimExtCapV320CRS1 = cIetfPimExtCapV320CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PIM-EXT-CAPABILITY", cIetfPimExtCapV320CRS1=cIetfPimExtCapV320CRS1, PYSNMP_MODULE_ID=ciscoIetfPimExtCapability, ciscoIetfPimExtCapability=ciscoIetfPimExtCapability)
