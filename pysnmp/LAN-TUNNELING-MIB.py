#
# PySNMP MIB module LAN-TUNNELING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LAN-TUNNELING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
pgainDSLAM, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainDSLAM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, ObjectIdentity, Counter32, Integer32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter64, Bits, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "ObjectIdentity", "Counter32", "Integer32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter64", "Bits", "MibIdentifier", "IpAddress")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
pgLantMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 2))
if mibBuilder.loadTexts: pgLantMIB.setLastUpdated('9712180000Z')
if mibBuilder.loadTexts: pgLantMIB.setOrganization('Pairgain Technology')
pgLantObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1))
class PgLantEncapType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("llc-snap", 2), ("vc-mux", 3))

pgLantTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1), )
if mibBuilder.loadTexts: pgLantTable.setStatus('current')
pgLantEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1), ).setIndexNames((0, "LAN-TUNNELING-MIB", "pgLantChannelPortIfIndex"))
if mibBuilder.loadTexts: pgLantEntry.setStatus('current')
pgLantChannelPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2047))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgLantChannelPortIfIndex.setStatus('current')
pgLantLinePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2047))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgLantLinePortIfIndex.setStatus('current')
pgLantVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgLantVpi.setStatus('current')
pgLantVci = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgLantVci.setStatus('current')
pgLantEncapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 5), PgLantEncapType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgLantEncapMode.setStatus('current')
pgLantRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pgLantRowStatus.setStatus('current')
mibBuilder.exportSymbols("LAN-TUNNELING-MIB", pgLantTable=pgLantTable, PgLantEncapType=PgLantEncapType, pgLantEntry=pgLantEntry, pgLantLinePortIfIndex=pgLantLinePortIfIndex, pgLantVpi=pgLantVpi, pgLantEncapMode=pgLantEncapMode, pgLantRowStatus=pgLantRowStatus, pgLantChannelPortIfIndex=pgLantChannelPortIfIndex, PYSNMP_MODULE_ID=pgLantMIB, pgLantObjects=pgLantObjects, pgLantMIB=pgLantMIB, pgLantVci=pgLantVci)
