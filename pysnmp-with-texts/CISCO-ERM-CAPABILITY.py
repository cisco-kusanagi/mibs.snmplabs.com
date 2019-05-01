#
# PySNMP MIB module CISCO-ERM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ERM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, ObjectIdentity, Unsigned32, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, Counter64, iso, Bits, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "iso", "Bits", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoErmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 492))
ciscoErmCapability.setRevisions(('2006-03-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoErmCapability.setRevisionsDescriptions(('Initial version of the capability MIB for the ERM MIB module',))
if mibBuilder.loadTexts: ciscoErmCapability.setLastUpdated('200603090000Z')
if mibBuilder.loadTexts: ciscoErmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoErmCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA E-mail: cs-erm@cisco.com')
if mibBuilder.loadTexts: ciscoErmCapability.setDescription('Agent capabilities for CISCO-ERM-MIB')
ciscoErmCapabilityV12R02SR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 492, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErmCapabilityV12R02SR = ciscoErmCapabilityV12R02SR.setProductRelease('Cisco IOS 12.2SR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErmCapabilityV12R02SR = ciscoErmCapabilityV12R02SR.setStatus('current')
if mibBuilder.loadTexts: ciscoErmCapabilityV12R02SR.setDescription('Cisco ERM Capabilities for IOS 12.2SR')
mibBuilder.exportSymbols("CISCO-ERM-CAPABILITY", ciscoErmCapability=ciscoErmCapability, ciscoErmCapabilityV12R02SR=ciscoErmCapabilityV12R02SR, PYSNMP_MODULE_ID=ciscoErmCapability)
