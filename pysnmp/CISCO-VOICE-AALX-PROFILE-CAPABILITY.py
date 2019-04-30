#
# PySNMP MIB module CISCO-VOICE-AALX-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-AALX-PROFILE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, Counter64, TimeTicks, Unsigned32, MibIdentifier, Counter32, IpAddress, ModuleIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter32", "IpAddress", "ModuleIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoiceAalxProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 352))
ciscoVoiceAalxProfileCapability.setRevisions(('2004-02-07 00:00',))
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setLastUpdated('200402070000Z')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setOrganization('Cisco Systems, Inc.')
cVoiceAalxProfileCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 352, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-AALX-PROFILE-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceAalxProfileCapability, cVoiceAalxProfileCapV5R00=cVoiceAalxProfileCapV5R00, ciscoVoiceAalxProfileCapability=ciscoVoiceAalxProfileCapability)
