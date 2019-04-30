#
# PySNMP MIB module CL-PKTC-EUE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CL-PKTC-EUE-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:08:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
pktcEUEMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcEUEMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Integer32, NotificationType, IpAddress, MibIdentifier, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Unsigned32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Integer32", "NotificationType", "IpAddress", "MibIdentifier", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Unsigned32", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
pktcEUETCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1))
if mibBuilder.loadTexts: pktcEUETCMIB.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: pktcEUETCMIB.setOrganization('Cable Television Laboratories, Inc.')
pktcEUETCNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 0))
pktcEUETCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1))
pktcEUETCConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2))
pktcEUETCCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 1))
pktcEUETCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 2))
pktcEUETCUsageObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1))
class PktcEUETCID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1023)

class PktcEUETCIDType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("gruu", 2), ("publicIdentity", 3), ("privateIdentity", 4), ("publicPrivatePair", 5), ("username", 6), ("macaddress", 7), ("packetcableIdentity", 8))

class PktcEUETCActStatus(TruthValue):
    status = 'current'

class PktcEUETCActStatusInfo(SnmpAdminString):
    status = 'current'
    subtypeSpec = SnmpAdminString.subtypeSpec + ValueSizeConstraint(1, 31)

class PktcEUETCUsrElementIndexType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 63)

class PktcEUETCAppOrgIdentifier(TextualConvention, Unsigned32):
    reference = 'http://www.iana.org/assignments/enterprise-numbers'
    status = 'current'

class PktcEUETCAppIdentifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 127)

class PktcEUETCUsrAppIndexType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

class PktcEUETCCredsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("none", 2), ("password", 3), ("preSharedKey", 4), ("certificate", 5))

class PktcEUETCCreds(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8192)

pktcEUETCSampleID = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 2), PktcEUETCID())
if mibBuilder.loadTexts: pktcEUETCSampleID.setStatus('obsolete')
pktcEUETCSampleIDType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 3), PktcEUETCIDType())
if mibBuilder.loadTexts: pktcEUETCSampleIDType.setStatus('obsolete')
pktcEUETCSampleActStatus = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 4), PktcEUETCActStatus())
if mibBuilder.loadTexts: pktcEUETCSampleActStatus.setStatus('obsolete')
pktcEUETCSampleUsrRef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 5), PktcEUETCUsrElementIndexType())
if mibBuilder.loadTexts: pktcEUETCSampleUsrRef.setStatus('obsolete')
pktcEUETCSampleCredsType = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 6), PktcEUETCCredsType())
if mibBuilder.loadTexts: pktcEUETCSampleCredsType.setStatus('obsolete')
pktcEUETCSampleCreds = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 7), PktcEUETCCreds())
if mibBuilder.loadTexts: pktcEUETCSampleCreds.setStatus('obsolete')
pktcEUETCSampleAppRef = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 8), PktcEUETCUsrAppIndexType())
if mibBuilder.loadTexts: pktcEUETCSampleAppRef.setStatus('obsolete')
pktcEUETCSampleActStatusInfo = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 9), PktcEUETCActStatusInfo())
if mibBuilder.loadTexts: pktcEUETCSampleActStatusInfo.setStatus('obsolete')
pktcEUETCAppIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 10), PktcEUETCAppIdentifier())
if mibBuilder.loadTexts: pktcEUETCAppIdentifier.setStatus('obsolete')
pktcEUETCAppOrgIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 1, 1, 11), PktcEUETCAppOrgIdentifier())
if mibBuilder.loadTexts: pktcEUETCAppOrgIdentifier.setStatus('obsolete')
pktcEUETCMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 1, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEUETCMIBCompliance = pktcEUETCMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("CL-PKTC-EUE-TC-MIB", PktcEUETCUsrElementIndexType=PktcEUETCUsrElementIndexType, PktcEUETCUsrAppIndexType=PktcEUETCUsrAppIndexType, pktcEUETCUsageObjs=pktcEUETCUsageObjs, pktcEUETCGroups=pktcEUETCGroups, PktcEUETCIDType=PktcEUETCIDType, pktcEUETCSampleID=pktcEUETCSampleID, pktcEUETCSampleUsrRef=pktcEUETCSampleUsrRef, pktcEUETCSampleActStatusInfo=pktcEUETCSampleActStatusInfo, pktcEUETCMIBCompliance=pktcEUETCMIBCompliance, PktcEUETCAppOrgIdentifier=PktcEUETCAppOrgIdentifier, pktcEUETCConformance=pktcEUETCConformance, PktcEUETCActStatusInfo=PktcEUETCActStatusInfo, pktcEUETCAppOrgIdentifier=pktcEUETCAppOrgIdentifier, pktcEUETCCompliances=pktcEUETCCompliances, pktcEUETCSampleAppRef=pktcEUETCSampleAppRef, pktcEUETCObjects=pktcEUETCObjects, pktcEUETCSampleCreds=pktcEUETCSampleCreds, pktcEUETCAppIdentifier=pktcEUETCAppIdentifier, PktcEUETCAppIdentifier=PktcEUETCAppIdentifier, PktcEUETCActStatus=PktcEUETCActStatus, pktcEUETCNotifications=pktcEUETCNotifications, PktcEUETCCreds=PktcEUETCCreds, PYSNMP_MODULE_ID=pktcEUETCMIB, pktcEUETCMIB=pktcEUETCMIB, pktcEUETCSampleIDType=pktcEUETCSampleIDType, pktcEUETCSampleCredsType=pktcEUETCSampleCredsType, pktcEUETCSampleActStatus=pktcEUETCSampleActStatus, PktcEUETCCredsType=PktcEUETCCredsType, PktcEUETCID=PktcEUETCID)
