#
# PySNMP MIB module CISCO-IP-FORWARD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-FORWARD-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Integer32, Counter32, IpAddress, iso, Bits, ObjectIdentity, ModuleIdentity, Gauge32, Unsigned32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Integer32", "Counter32", "IpAddress", "iso", "Bits", "ObjectIdentity", "ModuleIdentity", "Gauge32", "Unsigned32", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpForwardCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 595))
ciscoIpForwardCapability.setRevisions(('2010-09-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpForwardCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpForwardCapability.setLastUpdated('201009230000Z')
if mibBuilder.loadTexts: ciscoIpForwardCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpForwardCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipv6@cisco.com')
if mibBuilder.loadTexts: ciscoIpForwardCapability.setDescription('The capabilities description of IP-FORWARD-MIB.')
ciscoIpForwardCapabilityV12R2SE = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 595, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpForwardCapabilityV12R2SE = ciscoIpForwardCapabilityV12R2SE.setProductRelease('Cisco IOS 12.2SE Catalyst 2k/3k series.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpForwardCapabilityV12R2SE = ciscoIpForwardCapabilityV12R2SE.setStatus('current')
if mibBuilder.loadTexts: ciscoIpForwardCapabilityV12R2SE.setDescription('IP-FORWARD-MIB capabilities for Catalyst 2k/3k.')
mibBuilder.exportSymbols("CISCO-IP-FORWARD-CAPABILITY", ciscoIpForwardCapability=ciscoIpForwardCapability, PYSNMP_MODULE_ID=ciscoIpForwardCapability, ciscoIpForwardCapabilityV12R2SE=ciscoIpForwardCapabilityV12R2SE)
