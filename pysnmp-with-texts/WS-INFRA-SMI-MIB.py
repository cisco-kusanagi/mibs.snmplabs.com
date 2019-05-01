#
# PySNMP MIB module WS-INFRA-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WS-INFRA-SMI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:37:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, iso, ModuleIdentity, Unsigned32, MibIdentifier, IpAddress, Integer32, TimeTicks, Counter32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "iso", "ModuleIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wsInfra, = mibBuilder.importSymbols("WS-SMI", "wsInfra")
wslInfraMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 388, 14, 1, 1))
wslInfraMIB.setRevisions(('2008-05-01 13:27', '2007-01-12 11:54', '2006-05-24 14:42', '2005-12-19 10:35', '2005-07-28 19:00', '2005-06-24 11:00', '2005-06-22 11:36', '2005-05-23 17:36', '2005-05-04 16:09', '2005-05-04 15:58', '2005-05-04 10:32',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wslInfraMIB.setRevisionsDescriptions(('02a02 Added wsInfraSmtpNotify', '02a01', '01a09', '01a08', '01a07', '01a06', '01a05', '01a04', '01a03', '01a02', '01a01',))
if mibBuilder.loadTexts: wslInfraMIB.setLastUpdated('200805011900Z')
if mibBuilder.loadTexts: wslInfraMIB.setOrganization('Symbol Technology')
if mibBuilder.loadTexts: wslInfraMIB.setContactInfo('Symbol Technologies, Inc. Customer Service Postal: One Symbol Plaza Holtsville, NY 11742-1300 USA Tel: +1. 631.738.6213 E-mail: support@symbol.com Web: http://www.symbol.com/support')
if mibBuilder.loadTexts: wslInfraMIB.setDescription('infrastructure MIB')
wsInfraFileMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2))
wsInfraSysMsg = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 3))
wsInfraPM = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 5))
wsInfraDiag = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 6))
wsInfraCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 8))
wsInfraLic = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 9))
wsInfraNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 10))
wsInfraAutoUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 11))
wsInfraSmtpNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 12))
mibBuilder.exportSymbols("WS-INFRA-SMI-MIB", PYSNMP_MODULE_ID=wslInfraMIB, wsInfraSmtpNotify=wsInfraSmtpNotify, wsInfraNTP=wsInfraNTP, wslInfraMIB=wslInfraMIB, wsInfraCluster=wsInfraCluster, wsInfraDiag=wsInfraDiag, wsInfraLic=wsInfraLic, wsInfraFileMgmt=wsInfraFileMgmt, wsInfraPM=wsInfraPM, wsInfraAutoUpdate=wsInfraAutoUpdate, wsInfraSysMsg=wsInfraSysMsg)
