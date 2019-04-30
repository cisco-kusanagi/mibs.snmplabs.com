#
# PySNMP MIB module CISCO-VOICE-DIAL-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-DIAL-CONTROL-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Unsigned32, TimeTicks, Gauge32, Counter64, NotificationType, Bits, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "TimeTicks", "Gauge32", "Counter64", "NotificationType", "Bits", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoVoiceDialControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 83))
ciscoVoiceDialControlCapability.setRevisions(('2009-03-31 00:00', '2006-11-16 00:00', '2005-07-25 00:00', '1999-07-12 00:00', '1998-01-09 00:00', '1997-06-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setLastUpdated('200903310000Z')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setOrganization('Cisco Systems, Inc.')
ciscoVoiceDialControlCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03 = ciscoVoiceDialControlCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03 = ciscoVoiceDialControlCapabilityV11R03.setStatus('obsolete')
ciscoVoiceDialControlCapabilityV11R03Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03Rev1 = ciscoVoiceDialControlCapabilityV11R03Rev1.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03Rev1 = ciscoVoiceDialControlCapabilityV11R03Rev1.setStatus('current')
ciscoVoiceDialControlCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00 = ciscoVoiceDialControlCapabilityV12R00.setProductRelease('Cisco IOS 12.0(5)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00 = ciscoVoiceDialControlCapabilityV12R00.setStatus('obsolete')
ciscoVoiceDialControlCapabilityV12R00Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00Rev1 = ciscoVoiceDialControlCapabilityV12R00Rev1.setProductRelease('Cisco IOS 12.0(5)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00Rev1 = ciscoVoiceDialControlCapabilityV12R00Rev1.setStatus('current')
ciscoVoiceDialControlCapabilityV124R03T5400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV124R03T5400 = ciscoVoiceDialControlCapabilityV124R03T5400.setProductRelease('Cisco IOS 12.4(3)T on AS5400')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV124R03T5400 = ciscoVoiceDialControlCapabilityV124R03T5400.setStatus('current')
ciscoVoiceDialControlCapV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04 = ciscoVoiceDialControlCapV12R04.setProductRelease('Cisco IOS 12.4 for all platforms except IAD2420')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04 = ciscoVoiceDialControlCapV12R04.setStatus('current')
ciscoVoiceDialControlCapV12R04Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04Rev1 = ciscoVoiceDialControlCapV12R04Rev1.setProductRelease('Cisco IOS 12.4T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04Rev1 = ciscoVoiceDialControlCapV12R04Rev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-DIAL-CONTROL-CAPABILITY", ciscoVoiceDialControlCapV12R04Rev1=ciscoVoiceDialControlCapV12R04Rev1, ciscoVoiceDialControlCapability=ciscoVoiceDialControlCapability, ciscoVoiceDialControlCapabilityV11R03=ciscoVoiceDialControlCapabilityV11R03, PYSNMP_MODULE_ID=ciscoVoiceDialControlCapability, ciscoVoiceDialControlCapabilityV11R03Rev1=ciscoVoiceDialControlCapabilityV11R03Rev1, ciscoVoiceDialControlCapabilityV124R03T5400=ciscoVoiceDialControlCapabilityV124R03T5400, ciscoVoiceDialControlCapabilityV12R00Rev1=ciscoVoiceDialControlCapabilityV12R00Rev1, ciscoVoiceDialControlCapV12R04=ciscoVoiceDialControlCapV12R04, ciscoVoiceDialControlCapabilityV12R00=ciscoVoiceDialControlCapabilityV12R00)
