#
# PySNMP MIB module CISCO-HARDWARE-IP-VERIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HARDWARE-IP-VERIFY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, NotificationType, Counter64, TimeTicks, Unsigned32, IpAddress, Bits, Counter32, ObjectIdentity, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "NotificationType", "Counter64", "TimeTicks", "Unsigned32", "IpAddress", "Bits", "Counter32", "ObjectIdentity", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoHardwareIpVerifyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 804))
ciscoHardwareIpVerifyMIB.setRevisions(('2012-09-04 00:00',))
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyMIB.setOrganization('Cisco Systems, Inc.')
ciscoHardwareIpVerifyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 0))
ciscoHardwareIpVerifyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 1))
ciscoHardwareIpVerifyMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2))
chivIpVerifyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1), )
if mibBuilder.loadTexts: chivIpVerifyTable.setStatus('current')
chivIpVerifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1), ).setIndexNames((0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckIpType"), (0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckTypeName"))
if mibBuilder.loadTexts: chivIpVerifyEntry.setStatus('current')
chivIpVerifyCheckIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: chivIpVerifyCheckIpType.setStatus('current')
chivIpVerifyCheckTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("addressSrcBroadcast", 1), ("addressSrcMulticast", 2), ("addressDestZero", 3), ("addressIdentical", 4), ("addressSrcReserved", 5), ("addressClassE", 6), ("checksum", 7), ("protocol", 8), ("fragment", 9), ("lengthMinimum", 10), ("lengthConsistent", 11), ("lengthMaximumFragment", 12), ("lengthMaximumUdp", 13), ("lengthMaximumTcp", 14), ("tcpFlags", 15), ("tcpTinyFlags", 16), ("version", 17))))
if mibBuilder.loadTexts: chivIpVerifyCheckTypeName.setStatus('current')
chivIpVerifyCheckStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chivIpVerifyCheckStatus.setStatus('current')
chivIpVerifyPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chivIpVerifyPacketsDropped.setStatus('current')
ciscoHardwareIpVerifyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1))
ciscoHardwareIpVerifyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2))
ciscoHardwareIpVerifyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1, 1)).setObjects(("CISCO-HARDWARE-IP-VERIFY-MIB", "ciscoHardwareIpVerifyMIBStatisticGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHardwareIpVerifyMIBCompliance = ciscoHardwareIpVerifyMIBCompliance.setStatus('current')
ciscoHardwareIpVerifyMIBStatisticGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2, 1)).setObjects(("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckStatus"), ("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyPacketsDropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHardwareIpVerifyMIBStatisticGroup = ciscoHardwareIpVerifyMIBStatisticGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-HARDWARE-IP-VERIFY-MIB", chivIpVerifyTable=chivIpVerifyTable, chivIpVerifyCheckStatus=chivIpVerifyCheckStatus, chivIpVerifyEntry=chivIpVerifyEntry, chivIpVerifyPacketsDropped=chivIpVerifyPacketsDropped, ciscoHardwareIpVerifyMIBStatisticGroup=ciscoHardwareIpVerifyMIBStatisticGroup, ciscoHardwareIpVerifyMIBObjects=ciscoHardwareIpVerifyMIBObjects, ciscoHardwareIpVerifyMIBConform=ciscoHardwareIpVerifyMIBConform, ciscoHardwareIpVerifyMIB=ciscoHardwareIpVerifyMIB, chivIpVerifyCheckTypeName=chivIpVerifyCheckTypeName, chivIpVerifyCheckIpType=chivIpVerifyCheckIpType, ciscoHardwareIpVerifyMIBGroups=ciscoHardwareIpVerifyMIBGroups, ciscoHardwareIpVerifyMIBNotifs=ciscoHardwareIpVerifyMIBNotifs, PYSNMP_MODULE_ID=ciscoHardwareIpVerifyMIB, ciscoHardwareIpVerifyMIBCompliance=ciscoHardwareIpVerifyMIBCompliance, ciscoHardwareIpVerifyMIBCompliances=ciscoHardwareIpVerifyMIBCompliances)
