#
# PySNMP MIB module ELTEX-MES-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-SMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:01:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, ModuleIdentity, IpAddress, Counter64, Integer32, TimeTicks, ObjectIdentity, NotificationType, Unsigned32, iso, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "ModuleIdentity", "IpAddress", "Counter64", "Integer32", "TimeTicks", "ObjectIdentity", "NotificationType", "Unsigned32", "iso", "Gauge32", "MibIdentifier")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
class EltPortCopyRemoteDirectionType(TextualConvention, Integer32):
    description = 'copy remote direction type: 1- Rx 2- Tx'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eltPortCopyRemoteRx", 1), ("eltPortCopyRemoteTx", 2))

eltMesSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84))
eltMesSmon.setRevisions(('2016-02-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltMesSmon.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: eltMesSmon.setLastUpdated('201602100000Z')
if mibBuilder.loadTexts: eltMesSmon.setOrganization('Eltex Enterprise, Ltd.')
if mibBuilder.loadTexts: eltMesSmon.setContactInfo('www.eltex.nsk.ru')
if mibBuilder.loadTexts: eltMesSmon.setDescription('This private MIB module defines SMON private MIBs.')
eltPortCopyRemoteTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1), )
if mibBuilder.loadTexts: eltPortCopyRemoteTable.setStatus('current')
if mibBuilder.loadTexts: eltPortCopyRemoteTable.setDescription('A supplementing table for eltPortCopyRemoteTable.')
eltPortCopyRemoteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1), ).setIndexNames((0, "ELTEX-MES-SMON-MIB", "eltPortCopyRemoteDirection"))
if mibBuilder.loadTexts: eltPortCopyRemoteEntry.setStatus('current')
if mibBuilder.loadTexts: eltPortCopyRemoteEntry.setDescription('Each entry specifies vlan tag and user priority added by analyzer to a mirrored Rx/Tx packets.')
eltPortCopyRemoteDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 1), EltPortCopyRemoteDirectionType())
if mibBuilder.loadTexts: eltPortCopyRemoteDirection.setStatus('current')
if mibBuilder.loadTexts: eltPortCopyRemoteDirection.setDescription('This field defines a direction')
eltPortCopyRemoteVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPortCopyRemoteVlan.setStatus('current')
if mibBuilder.loadTexts: eltPortCopyRemoteVlan.setDescription('This field defines an RSPAN VLAN id')
eltPortCopyRemotePrio = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPortCopyRemotePrio.setStatus('current')
if mibBuilder.loadTexts: eltPortCopyRemotePrio.setDescription('This field defines an RSPAN user priority')
eltPortCopyRemoteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltPortCopyRemoteStatus.setStatus('current')
if mibBuilder.loadTexts: eltPortCopyRemoteStatus.setDescription('This field defines a row status')
mibBuilder.exportSymbols("ELTEX-MES-SMON-MIB", eltPortCopyRemoteStatus=eltPortCopyRemoteStatus, eltPortCopyRemoteVlan=eltPortCopyRemoteVlan, PYSNMP_MODULE_ID=eltMesSmon, eltPortCopyRemoteDirection=eltPortCopyRemoteDirection, EltPortCopyRemoteDirectionType=EltPortCopyRemoteDirectionType, eltPortCopyRemotePrio=eltPortCopyRemotePrio, eltPortCopyRemoteTable=eltPortCopyRemoteTable, eltPortCopyRemoteEntry=eltPortCopyRemoteEntry, eltMesSmon=eltMesSmon)
