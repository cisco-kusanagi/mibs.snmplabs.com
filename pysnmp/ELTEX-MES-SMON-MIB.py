#
# PySNMP MIB module ELTEX-MES-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-SMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, iso, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, Bits, Integer32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Integer32", "Counter32", "IpAddress")
TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
class EltPortCopyRemoteDirectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eltPortCopyRemoteRx", 1), ("eltPortCopyRemoteTx", 2))

eltMesSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84))
eltMesSmon.setRevisions(('2016-02-10 00:00',))
if mibBuilder.loadTexts: eltMesSmon.setLastUpdated('201602100000Z')
if mibBuilder.loadTexts: eltMesSmon.setOrganization('Eltex Enterprise, Ltd.')
eltPortCopyRemoteTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1), )
if mibBuilder.loadTexts: eltPortCopyRemoteTable.setStatus('current')
eltPortCopyRemoteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1), ).setIndexNames((0, "ELTEX-MES-SMON-MIB", "eltPortCopyRemoteDirection"))
if mibBuilder.loadTexts: eltPortCopyRemoteEntry.setStatus('current')
eltPortCopyRemoteDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 1), EltPortCopyRemoteDirectionType())
if mibBuilder.loadTexts: eltPortCopyRemoteDirection.setStatus('current')
eltPortCopyRemoteVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPortCopyRemoteVlan.setStatus('current')
eltPortCopyRemotePrio = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPortCopyRemotePrio.setStatus('current')
eltPortCopyRemoteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltPortCopyRemoteStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-SMON-MIB", eltMesSmon=eltMesSmon, EltPortCopyRemoteDirectionType=EltPortCopyRemoteDirectionType, eltPortCopyRemoteEntry=eltPortCopyRemoteEntry, PYSNMP_MODULE_ID=eltMesSmon, eltPortCopyRemotePrio=eltPortCopyRemotePrio, eltPortCopyRemoteStatus=eltPortCopyRemoteStatus, eltPortCopyRemoteDirection=eltPortCopyRemoteDirection, eltPortCopyRemoteVlan=eltPortCopyRemoteVlan, eltPortCopyRemoteTable=eltPortCopyRemoteTable)
