#
# PySNMP MIB module CISCO-XGCP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-XGCP-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, NotificationType, TimeTicks, Counter64, iso, Counter32, MibIdentifier, ObjectIdentity, ModuleIdentity, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "NotificationType", "TimeTicks", "Counter64", "iso", "Counter32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Integer32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoXgcpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoXgcpExtCapability.setRevisions(('2004-06-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoXgcpExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setLastUpdated('200406180000Z')
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setDescription('The capabilities description of CISCO-XGCP-EXT-MIB.')
ciscoXgcpExtCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpExtCapabilityV12R03 = ciscoXgcpExtCapabilityV12R03.setProductRelease('Cisco IOS 12.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpExtCapabilityV12R03 = ciscoXgcpExtCapabilityV12R03.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpExtCapabilityV12R03.setDescription('CISCO-XGCP-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-XGCP-EXT-CAPABILITY", ciscoXgcpExtCapability=ciscoXgcpExtCapability, PYSNMP_MODULE_ID=ciscoXgcpExtCapability, ciscoXgcpExtCapabilityV12R03=ciscoXgcpExtCapabilityV12R03)
