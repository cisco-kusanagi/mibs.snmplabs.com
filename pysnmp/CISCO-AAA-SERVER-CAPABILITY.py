#
# PySNMP MIB module CISCO-AAA-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAA-SERVER-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, TimeTicks, MibIdentifier, Gauge32, Unsigned32, IpAddress, Bits, Counter32, Integer32, iso, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Gauge32", "Unsigned32", "IpAddress", "Bits", "Counter32", "Integer32", "iso", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAAAServerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 129))
ciscoAAAServerCapability.setRevisions(('2008-07-21 00:00', '2006-02-21 00:00', '2003-11-14 00:00', '2000-01-20 00:00',))
if mibBuilder.loadTexts: ciscoAAAServerCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoAAAServerCapability.setOrganization('Cisco Systems, Inc.')
ciscoAAAServerCapabilityV10R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityV10R00 = ciscoAAAServerCapabilityV10R00.setProductRelease('Cisco IOS 12.0(4)XJ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityV10R00 = ciscoAAAServerCapabilityV10R00.setStatus('current')
ciscoAAAServerCapabilityMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityMDS13R1 = ciscoAAAServerCapabilityMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityMDS13R1 = ciscoAAAServerCapabilityMDS13R1.setStatus('current')
ciscoAAAServerCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityACSWV03R000 = ciscoAAAServerCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityACSWV03R000 = ciscoAAAServerCapabilityACSWV03R000.setStatus('current')
ciscoAAAServerCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapc4710aceVA1R70 = ciscoAAAServerCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapc4710aceVA1R70 = ciscoAAAServerCapc4710aceVA1R70.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-SERVER-CAPABILITY", ciscoAAAServerCapabilityACSWV03R000=ciscoAAAServerCapabilityACSWV03R000, ciscoAAAServerCapc4710aceVA1R70=ciscoAAAServerCapc4710aceVA1R70, ciscoAAAServerCapability=ciscoAAAServerCapability, ciscoAAAServerCapabilityMDS13R1=ciscoAAAServerCapabilityMDS13R1, ciscoAAAServerCapabilityV10R00=ciscoAAAServerCapabilityV10R00, PYSNMP_MODULE_ID=ciscoAAAServerCapability)
