#
# PySNMP MIB module CISCO-VLAN-TRANSLATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-TRANSLATION-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, iso, Gauge32, Counter32, TimeTicks, Bits, ObjectIdentity, NotificationType, Integer32, Counter64, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "iso", "Gauge32", "Counter32", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType", "Integer32", "Counter64", "ModuleIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVlanTranslationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 405))
ciscoVlanTranslationCapability.setRevisions(('2012-01-09 00:00', '2006-02-08 00:00', '2004-08-11 00:00', '2004-06-07 00:00',))
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setLastUpdated('201201090000Z')
if mibBuilder.loadTexts: ciscoVlanTranslationCapability.setOrganization('Cisco Systems, Inc.')
cVlanTranslationCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTranslationCapCatOSV08R0401 = cVlanTranslationCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTranslationCapCatOSV08R0401 = cVlanTranslationCapCatOSV08R0401.setStatus('current')
cVlanTransCapV12R0218SXEPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV12R0218SXEPCat6K = cVlanTransCapV12R0218SXEPCat6K.setProductRelease('Cisco IOS 12.2(18)SXE on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV12R0218SXEPCat6K = cVlanTransCapV12R0218SXEPCat6K.setStatus('current')
cVlanTransCapV15R0001SYPCat6kSup2T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 405, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV15R0001SYPCat6kSup2T = cVlanTransCapV15R0001SYPCat6kSup2T.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                     series devices with Supervisor 2T present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVlanTransCapV15R0001SYPCat6kSup2T = cVlanTransCapV15R0001SYPCat6kSup2T.setStatus('current')
mibBuilder.exportSymbols("CISCO-VLAN-TRANSLATION-CAPABILITY", ciscoVlanTranslationCapability=ciscoVlanTranslationCapability, PYSNMP_MODULE_ID=ciscoVlanTranslationCapability, cVlanTransCapV15R0001SYPCat6kSup2T=cVlanTransCapV15R0001SYPCat6kSup2T, cVlanTransCapV12R0218SXEPCat6K=cVlanTransCapV12R0218SXEPCat6K, cVlanTranslationCapCatOSV08R0401=cVlanTranslationCapCatOSV08R0401)
