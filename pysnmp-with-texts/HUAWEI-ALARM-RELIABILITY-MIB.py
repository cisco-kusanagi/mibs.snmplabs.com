#
# PySNMP MIB module HUAWEI-ALARM-RELIABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-ALARM-RELIABILITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Counter64, Bits, ObjectIdentity, ModuleIdentity, TimeTicks, Counter32, Gauge32, NotificationType, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Counter64", "Bits", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter32", "Gauge32", "NotificationType", "iso", "Integer32")
RowStatus, TextualConvention, DisplayString, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TimeInterval")
hwARModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141))
hwARModule.setRevisions(('2006-12-14 20:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwARModule.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hwARModule.setLastUpdated('200612142010Z')
if mibBuilder.loadTexts: hwARModule.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwARModule.setContactInfo('VRP Team Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwARModule.setDescription('The HUAWEI-ALARM-RELIABILITY-MIB contains all objects to manager Notification packets, it mainly contains following parts: 1) The number of pending Inform packets. 2) The default retry number. 3) The timeout apply to all target hosts. ')
hwAR = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1))
hwARInformPendings = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)).clone(39)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwARInformPendings.setStatus('current')
if mibBuilder.loadTexts: hwARInformPendings.setDescription("If a pending inform packet receives the response packet and its request-id is equal to pending packet's, this pending packet is discarded at once. otherwise, it will try to retransmit the Inform packet after snmpTargetAddrTimeout[RFC3413], repeat this operation snmpTargetAddrRetryCount [RFC3413] numbers if a response is not received for a generated message. After this, this pending packet will be discarded.")
hwARRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwARRetryCount.setStatus('current')
if mibBuilder.loadTexts: hwARRetryCount.setDescription('This object specifies a default number of retries to be attempted when a response is not received for a generated message. Note that, this number will apply on all the target host')
hwARTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 1, 3), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(100, 180000)).clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwARTimeout.setStatus('current')
if mibBuilder.loadTexts: hwARTimeout.setDescription('This object should reflect the expected maximum round trip time for communicating with the target hosts. When a message is send to the target hosts, and response (if expected) are not received within this time period, an implementation may assume that the response will not be delivered. Note that this time interval will apply to all target host.')
hwARConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2))
hwARCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 1))
hwARCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 1, 1)).setObjects(("HUAWEI-ALARM-RELIABILITY-MIB", "hwARInformPacketsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwARCompliance = hwARCompliance.setStatus('current')
if mibBuilder.loadTexts: hwARCompliance.setDescription('The compliance statement for systems supporting the this module.')
hwARGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 2))
hwARInformPacketsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 141, 2, 2, 1)).setObjects(("HUAWEI-ALARM-RELIABILITY-MIB", "hwARInformPendings"), ("HUAWEI-ALARM-RELIABILITY-MIB", "hwARRetryCount"), ("HUAWEI-ALARM-RELIABILITY-MIB", "hwARTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwARInformPacketsGroup = hwARInformPacketsGroup.setStatus('current')
if mibBuilder.loadTexts: hwARInformPacketsGroup.setDescription('The group of operating inform packets.')
mibBuilder.exportSymbols("HUAWEI-ALARM-RELIABILITY-MIB", hwARInformPendings=hwARInformPendings, hwARInformPacketsGroup=hwARInformPacketsGroup, hwARCompliance=hwARCompliance, hwARRetryCount=hwARRetryCount, PYSNMP_MODULE_ID=hwARModule, hwARTimeout=hwARTimeout, hwARModule=hwARModule, hwARConformance=hwARConformance, hwARCompliances=hwARCompliances, hwARGroups=hwARGroups, hwAR=hwAR)
