#
# PySNMP MIB module HUAWEI-ALARM-RELIABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-ALARM-RELIABILITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, IpAddress, Counter64, Bits, iso, Integer32, Counter32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter64", "Bits", "iso", "Integer32", "Counter32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Gauge32", "Unsigned32")
TimeInterval, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "DisplayString", "TextualConvention", "RowStatus")
hwARModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141))
hwARModule.setRevisions(('2006-12-14 20:10',))
if mibBuilder.loadTexts: hwARModule.setLastUpdated('200612142010Z')
if mibBuilder.loadTexts: hwARModule.setOrganization('Huawei Technologies co.,Ltd.')
hwAR = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1))
hwARInformPendings = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)).clone(39)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwARInformPendings.setStatus('current')
hwARRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwARRetryCount.setStatus('current')
hwARTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 3), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(100, 180000)).clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwARTimeout.setStatus('current')
hwARConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2))
hwARCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 1))
hwARCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 1, 1)).setObjects(("HUAWEI-ALARM-RELIABILITY-MIB", "hwARInformPacketsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwARCompliance = hwARCompliance.setStatus('current')
hwARGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 2))
hwARInformPacketsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 2, 1)).setObjects(("HUAWEI-ALARM-RELIABILITY-MIB", "hwARInformPendings"), ("HUAWEI-ALARM-RELIABILITY-MIB", "hwARRetryCount"), ("HUAWEI-ALARM-RELIABILITY-MIB", "hwARTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwARInformPacketsGroup = hwARInformPacketsGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-ALARM-RELIABILITY-MIB", hwARInformPendings=hwARInformPendings, hwARInformPacketsGroup=hwARInformPacketsGroup, hwARCompliances=hwARCompliances, hwARCompliance=hwARCompliance, hwARGroups=hwARGroups, PYSNMP_MODULE_ID=hwARModule, hwARTimeout=hwARTimeout, hwARModule=hwARModule, hwARConformance=hwARConformance, hwARRetryCount=hwARRetryCount, hwAR=hwAR)
