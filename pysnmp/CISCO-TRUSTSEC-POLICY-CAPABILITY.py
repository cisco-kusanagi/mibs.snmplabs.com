#
# PySNMP MIB module CISCO-TRUSTSEC-POLICY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-POLICY-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, ModuleIdentity, iso, Bits, MibIdentifier, IpAddress, Counter32, Gauge32, Unsigned32, TimeTicks, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "ModuleIdentity", "iso", "Bits", "MibIdentifier", "IpAddress", "Counter32", "Gauge32", "Unsigned32", "TimeTicks", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTrustSecPolicyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 601))
ciscoTrustSecPolicyCapability.setRevisions(('2013-05-01 00:00', '2013-01-09 00:00', '2010-11-16 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setLastUpdated('201305010000Z')
if mibBuilder.loadTexts: ciscoTrustSecPolicyCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecPolicyCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV12R0250SYPCat6k = ciscoTrustSecPolicyCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV12R0250SYPCat6k = ciscoTrustSecPolicyCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T.setStatus('current')
ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 601, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720 = ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-POLICY-CAPABILITY", ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T=ciscoTrustSecPolicyCapV15R0101SYPCat6kSup2T, ciscoTrustSecPolicyCapV12R0250SYPCat6k=ciscoTrustSecPolicyCapV12R0250SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecPolicyCapability, ciscoTrustSecPolicyCapability=ciscoTrustSecPolicyCapability, ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720=ciscoTrustSecPolicyCapV15R0101SYPCat6kSup720)
