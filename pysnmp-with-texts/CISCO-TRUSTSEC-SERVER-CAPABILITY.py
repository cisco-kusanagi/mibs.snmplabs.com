#
# PySNMP MIB module CISCO-TRUSTSEC-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-SERVER-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:14:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Bits, Counter64, Unsigned32, ObjectIdentity, Counter32, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Bits", "Counter64", "Unsigned32", "ObjectIdentity", "Counter32", "Gauge32", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoTrustSecServerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 596))
ciscoTrustSecServerCapability.setRevisions(('2012-09-07 00:00', '2010-10-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setRevisionsDescriptions(('Added capability statement ciscoTrustSecServerCapV15R0101SYPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setContactInfo('Cisco Systems, Inc Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setDescription('The capabilities description of CISCO-TRUSTSEC-SERVER-MIB.')
ciscoTrustSecServerCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 596, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV12R0250SYPCat6k = ciscoTrustSecServerCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV12R0250SYPCat6k = ciscoTrustSecServerCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecServerCapV12R0250SYPCat6k.setDescription('CISCO-TRUSTSEC-SERVER-MIB capabilities.')
ciscoTrustSecServerCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 596, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV15R0101SYPCat6k = ciscoTrustSecServerCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV15R0101SYPCat6k = ciscoTrustSecServerCapV15R0101SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoTrustSecServerCapV15R0101SYPCat6k.setDescription('CISCO-TRUSTSEC-SERVER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-SERVER-CAPABILITY", ciscoTrustSecServerCapV12R0250SYPCat6k=ciscoTrustSecServerCapV12R0250SYPCat6k, ciscoTrustSecServerCapability=ciscoTrustSecServerCapability, ciscoTrustSecServerCapV15R0101SYPCat6k=ciscoTrustSecServerCapV15R0101SYPCat6k, PYSNMP_MODULE_ID=ciscoTrustSecServerCapability)
