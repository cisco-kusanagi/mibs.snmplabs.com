#
# PySNMP MIB module CISCO-VOICE-AALX-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-AALX-PROFILE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, NotificationType, Unsigned32, MibIdentifier, Gauge32, ObjectIdentity, Counter32, IpAddress, iso, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "NotificationType", "Unsigned32", "MibIdentifier", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "iso", "Bits", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoiceAalxProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 352))
ciscoVoiceAalxProfileCapability.setRevisions(('2004-02-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setLastUpdated('200402070000Z')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setDescription('The agent capabilities for CISCO-VOICE-AALX-PROFILE-MIB.')
cVoiceAalxProfileCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 352, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setStatus('current')
if mibBuilder.loadTexts: cVoiceAalxProfileCapV5R00.setDescription('AALX Profile MIB capabilities for Voice Switch Service Module(VXSM) in release 5.0.0.')
mibBuilder.exportSymbols("CISCO-VOICE-AALX-PROFILE-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceAalxProfileCapability, ciscoVoiceAalxProfileCapability=ciscoVoiceAalxProfileCapability, cVoiceAalxProfileCapV5R00=cVoiceAalxProfileCapV5R00)
