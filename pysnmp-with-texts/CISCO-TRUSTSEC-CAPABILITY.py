#
# PySNMP MIB module CISCO-TRUSTSEC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
CtsPasswordEncryptionType, = mibBuilder.importSymbols("CISCO-TRUSTSEC-TC-MIB", "CtsPasswordEncryptionType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, TimeTicks, Gauge32, NotificationType, Counter32, ObjectIdentity, ModuleIdentity, Counter64, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "TimeTicks", "Gauge32", "NotificationType", "Counter32", "ObjectIdentity", "ModuleIdentity", "Counter64", "Bits", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoTrustSecCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 598))
ciscoTrustSecCapability.setRevisions(('2012-09-07 00:00', '2011-09-28 00:00', '2010-11-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecCapability.setRevisionsDescriptions(('Added capability statements - ciscoTrustSecCapV15R0101SYPCat6kSup2T - ciscoTrustSecCapV15R0101SYPCat6kSup720 Added VARITION for object ctsSgtAssignmentMethod to the following capability statements: - ciscoTrustSecCapV12R0250SYPCat6k - ciscoTrustSecCapV15R0001SYPCat6k', 'Added capability statement ciscoTrustSecCapV15R0001SYPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecCapability.setDescription('The capabilities description of CISCO-TRUSTSEC-MIB.')
ciscoTrustSecCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV12R0250SYPCat6k = ciscoTrustSecCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV12R0250SYPCat6k = ciscoTrustSecCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-MIB capabilities.')
ciscoTrustSecCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0001SYPCat6k = ciscoTrustSecCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0001SYPCat6k = ciscoTrustSecCapV15R0001SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecCapV15R0001SYPCat6k.setDescription('CISCO-TRUSTSEC-MIB capabilities.')
ciscoTrustSecCapV15R0101SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup2T = ciscoTrustSecCapV15R0101SYPCat6kSup2T.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup2T = ciscoTrustSecCapV15R0101SYPCat6kSup2T.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecCapV15R0101SYPCat6kSup2T.setDescription('CISCO-TRUSTSEC-MIB capabilities.')
ciscoTrustSecCapV15R0101SYPCat6kSup720 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 598, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup720 = ciscoTrustSecCapV15R0101SYPCat6kSup720.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 720 present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecCapV15R0101SYPCat6kSup720 = ciscoTrustSecCapV15R0101SYPCat6kSup720.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecCapV15R0101SYPCat6kSup720.setDescription('CISCO-TRUSTSEC-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-CAPABILITY", ciscoTrustSecCapV15R0001SYPCat6k=ciscoTrustSecCapV15R0001SYPCat6k, ciscoTrustSecCapV15R0101SYPCat6kSup720=ciscoTrustSecCapV15R0101SYPCat6kSup720, PYSNMP_MODULE_ID=ciscoTrustSecCapability, ciscoTrustSecCapV15R0101SYPCat6kSup2T=ciscoTrustSecCapV15R0101SYPCat6kSup2T, ciscoTrustSecCapability=ciscoTrustSecCapability, ciscoTrustSecCapV12R0250SYPCat6k=ciscoTrustSecCapV12R0250SYPCat6k)
