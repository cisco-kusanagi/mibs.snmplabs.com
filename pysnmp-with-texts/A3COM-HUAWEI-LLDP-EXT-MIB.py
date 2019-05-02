#
# PySNMP MIB module A3COM-HUAWEI-LLDP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-LLDP-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
LldpPortNumber, = mibBuilder.importSymbols("LLDP-MIB", "LldpPortNumber")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, Unsigned32, Gauge32, iso, ModuleIdentity, Integer32, Bits, IpAddress, Counter64, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Unsigned32", "Gauge32", "iso", "ModuleIdentity", "Integer32", "Bits", "IpAddress", "Counter64", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
h3clldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100))
h3clldp.setRevisions(('2009-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3clldp.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: h3clldp.setLastUpdated('200903210000Z')
if mibBuilder.loadTexts: h3clldp.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: h3clldp.setContactInfo('Platform Team H3C Technologies Co.,Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: h3clldp.setDescription('LLDP extended management infomation.')
h3clldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1))
h3clldpConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1))
h3clldpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3clldpAdminStatus.setStatus('current')
if mibBuilder.loadTexts: h3clldpAdminStatus.setDescription('The global administratively desired status of the local LLDP agent.')
h3clldpComplianceCDPStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3clldpComplianceCDPStatus.setStatus('current')
if mibBuilder.loadTexts: h3clldpComplianceCDPStatus.setDescription('The global administratively desired status of CDP Compliance.')
h3clldpPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3), )
if mibBuilder.loadTexts: h3clldpPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: h3clldpPortConfigTable.setDescription('The port-based table that controls extended functions.')
h3clldpPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-LLDP-EXT-MIB", "h3clldpPortConfigPortNum"))
if mibBuilder.loadTexts: h3clldpPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: h3clldpPortConfigEntry.setDescription('LLDP extended configuration information for a particular port. This co- nfiguration parameter controls compliance with other non-standard link layer discovery protocol such as CDP.')
h3clldpPortConfigPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: h3clldpPortConfigPortNum.setStatus('current')
if mibBuilder.loadTexts: h3clldpPortConfigPortNum.setDescription('The index value used to identify the port component associated with th- is entry.')
h3clldpPortConfigCDPComplianceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("txAndRx", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3clldpPortConfigCDPComplianceStatus.setStatus('current')
if mibBuilder.loadTexts: h3clldpPortConfigCDPComplianceStatus.setDescription("The administratively desired CDP Compliance status of the local LLDP a- gent. If the associated h3clldpPortConfigCDPComplianceStatus object has a value of 'txAndRx', then the LLDP agent will receive CDP frames on th- is port, and will transmit CDP frames only after receive a CDP frames. If the associated lldpPortConfigAdminStatus object has a value of 'disa- bled', LLDP agent will not transmit or receive CDP frames on this port.")
mibBuilder.exportSymbols("A3COM-HUAWEI-LLDP-EXT-MIB", h3clldpPortConfigEntry=h3clldpPortConfigEntry, PYSNMP_MODULE_ID=h3clldp, h3clldpPortConfigPortNum=h3clldpPortConfigPortNum, h3clldpConfiguration=h3clldpConfiguration, h3clldpAdminStatus=h3clldpAdminStatus, h3clldpPortConfigTable=h3clldpPortConfigTable, h3clldpPortConfigCDPComplianceStatus=h3clldpPortConfigCDPComplianceStatus, h3clldp=h3clldp, h3clldpComplianceCDPStatus=h3clldpComplianceCDPStatus, h3clldpObjects=h3clldpObjects)
