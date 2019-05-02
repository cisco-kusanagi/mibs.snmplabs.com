#
# PySNMP MIB module CISCO-TRUSTSEC-POLICY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-POLICY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, TimeTicks, ModuleIdentity, NotificationType, MibIdentifier, iso, Counter32, Counter64, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "TimeTicks", "ModuleIdentity", "NotificationType", "MibIdentifier", "iso", "Counter32", "Counter64", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTrustSecPolicyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 601))
ciscoTrustSecPolicyCapability.setRevisions(('2013-05-01 00:00', '2013-01-09 00:00', '2010-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setRevisionsDescriptions(('Added the following VARIATION clauses in capability statement ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720: - ctspPeerPolicyUpdatedNotifEnable - ctspOldPeerSgt - ctspPeerPolicyUpdatedNotif', 'Added capability statement ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T and ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setLastUpdated('201305010000Z')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setDescription('The capabilities description of CISCO-TRUSTSEC-POLICY-MIB.')
ciscoTrustSecPolicyCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV12R0250SYPCat6k = ciscoTrustSecPolicyCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV12R0250SYPCat6k = ciscoTrustSecPolicyCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-POLICY-MIB capabilities.')
ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setDescription('CISCO-TRUSTSEC-POLICY-MIB capabilities.')
ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setDescription('CISCO-TRUSTSEC-POLICY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-POLICY-CAPABILITY", ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720=ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720, ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T=ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T, PYSNMP_MODULE_ID=ciscoTrustSecPolicyCapability, ciscoTrustSecPolicyCapability=ciscoTrustSecPolicyCapability, ciscoTrustSecPolicyCapV12R0250SYPCat6k=ciscoTrustSecPolicyCapV12R0250SYPCat6k)
