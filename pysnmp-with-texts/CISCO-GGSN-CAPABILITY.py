#
# PySNMP MIB module CISCO-GGSN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GGSN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, ModuleIdentity, MibIdentifier, Integer32, iso, Counter32, Gauge32, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "ModuleIdentity", "MibIdentifier", "Integer32", "iso", "Counter32", "Gauge32", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cggsnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 296))
cggsnCapability.setRevisions(('2006-10-09 01:00', '2003-04-08 03:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cggsnCapability.setRevisionsDescriptions(('Added cggsnCapabilityV12R4M9XG.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cggsnCapability.setLastUpdated('200610090100Z')
if mibBuilder.loadTexts: cggsnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cggsnCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cggsnCapability.setDescription('Agent capabilities for CISCO-GGSN-MIB')
cggsnCapabilityV12R2M8YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YD = cggsnCapabilityV12R2M8YD.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YD = cggsnCapabilityV12R2M8YD.setStatus('current')
if mibBuilder.loadTexts: cggsnCapabilityV12R2M8YD.setDescription('Cisco GGSN MIB capabilities.')
cggsnCapabilityV12R2M8YY1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YY1 = cggsnCapabilityV12R2M8YY1.setProductRelease('Cisco IOS 12.2(8)YY1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YY1 = cggsnCapabilityV12R2M8YY1.setStatus('current')
if mibBuilder.loadTexts: cggsnCapabilityV12R2M8YY1.setDescription('Cisco GGSN MIB capabilities.')
cggsnCapabilityV12R2M8YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YW = cggsnCapabilityV12R2M8YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R2M8YW = cggsnCapabilityV12R2M8YW.setStatus('current')
if mibBuilder.loadTexts: cggsnCapabilityV12R2M8YW.setDescription('Cisco GGSN MIB capabilities.')
cggsnCapabilityV12R4M9XG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 296, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R4M9XG = cggsnCapabilityV12R4M9XG.setProductRelease('Cisco IOS 12.4(9)XG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnCapabilityV12R4M9XG = cggsnCapabilityV12R4M9XG.setStatus('current')
if mibBuilder.loadTexts: cggsnCapabilityV12R4M9XG.setDescription('Cisco GGSN MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GGSN-CAPABILITY", cggsnCapabilityV12R2M8YY1=cggsnCapabilityV12R2M8YY1, cggsnCapabilityV12R2M8YW=cggsnCapabilityV12R2M8YW, PYSNMP_MODULE_ID=cggsnCapability, cggsnCapability=cggsnCapability, cggsnCapabilityV12R4M9XG=cggsnCapabilityV12R4M9XG, cggsnCapabilityV12R2M8YD=cggsnCapabilityV12R2M8YD)
