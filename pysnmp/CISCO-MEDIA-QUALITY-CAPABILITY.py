#
# PySNMP MIB module CISCO-MEDIA-QUALITY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEDIA-QUALITY-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Bits, Integer32, IpAddress, Unsigned32, MibIdentifier, iso, ObjectIdentity, ModuleIdentity, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Bits", "Integer32", "IpAddress", "Unsigned32", "MibIdentifier", "iso", "ObjectIdentity", "ModuleIdentity", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMediaQualityCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 604))
ciscoMediaQualityCapability.setRevisions(('2011-09-23 00:00', '2011-04-15 00:00',))
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setLastUpdated('201109230000Z')
if mibBuilder.loadTexts: ciscoMediaQualityCapability.setOrganization('Cisco Systems, Inc.')
ciscoMediaQualityCapabilityV152R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 604, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R01 = ciscoMediaQualityCapabilityV152R01.setProductRelease('OS=IOS\n                     OSVERSION=15.2(1)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R01 = ciscoMediaQualityCapabilityV152R01.setStatus('current')
ciscoMediaQualityCapabilityV152R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 604, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R02 = ciscoMediaQualityCapabilityV152R02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c28xx,c3825,c3845,c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMediaQualityCapabilityV152R02 = ciscoMediaQualityCapabilityV152R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEDIA-QUALITY-CAPABILITY", ciscoMediaQualityCapabilityV152R01=ciscoMediaQualityCapabilityV152R01, ciscoMediaQualityCapabilityV152R02=ciscoMediaQualityCapabilityV152R02, PYSNMP_MODULE_ID=ciscoMediaQualityCapability, ciscoMediaQualityCapability=ciscoMediaQualityCapability)
