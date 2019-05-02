#
# PySNMP MIB module CISCO-VOICE-ANALOG-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-ANALOG-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, iso, Counter32, Bits, ModuleIdentity, Counter64, IpAddress, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "iso", "Counter32", "Bits", "ModuleIdentity", "Counter64", "IpAddress", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoiceAnalogIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 82))
ciscoVoiceAnalogIfCapability.setRevisions(('2003-04-28 00:00', '1997-06-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setRevisionsDescriptions(('cvaIfEMCfgLmrMCap & cvaIfEMCfgLmrECap are readonly', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setLastUpdated('200304280000Z')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setDescription('Agent capabilities for CISCO-VOICE-ANALOG-IF-MIB')
ciscoVoiceAnalogIfCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 82, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapabilityV11R03.setDescription('Cisco Voice Analog Interface MIB capabilities')
mibBuilder.exportSymbols("CISCO-VOICE-ANALOG-IF-CAPABILITY", ciscoVoiceAnalogIfCapability=ciscoVoiceAnalogIfCapability, ciscoVoiceAnalogIfCapabilityV11R03=ciscoVoiceAnalogIfCapabilityV11R03, PYSNMP_MODULE_ID=ciscoVoiceAnalogIfCapability)
