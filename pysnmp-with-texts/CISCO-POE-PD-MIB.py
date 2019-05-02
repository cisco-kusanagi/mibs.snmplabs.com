#
# PySNMP MIB module CISCO-POE-PD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-POE-PD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:09:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Gauge32, MibIdentifier, IpAddress, ModuleIdentity, Integer32, NotificationType, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Gauge32", "MibIdentifier", "IpAddress", "ModuleIdentity", "Integer32", "NotificationType", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPoePdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 414))
ciscoPoePdMIB.setRevisions(('2004-05-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPoePdMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPoePdMIB.setLastUpdated('200405050000Z')
if mibBuilder.loadTexts: ciscoPoePdMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoPoePdMIB.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-poe@cisco.com')
if mibBuilder.loadTexts: ciscoPoePdMIB.setDescription('This MIB is intended for devices powered by external power sources, in particular Power Over Ethernet (PoE or formerly called inline power), to provide power usage configuration and information for NMS. For example, PoE supplies DC power over standard Category 5 unshielded twisted-pair (UTP) cable. Instead of requiring wall power, powered devices such as IP telephones can utilize power provided from power source equipments. By using Cisco Discovery Protocol (CDP), powered devices can negotiated with power source equipment to obtain optimum power supply. GLOSSARY Midspan Injector The midspan PSE sends out a signal tone down one of the unused pairs of the standard Category 5 cable and detects tone on the other unused pair when the PD loops this tone back to it through a loopback transformer. Once the midspan PSE detects this tone, it begins to provide power down the cable using the unused pairs. The midspan PSE provide no physical layer capability. Powered Device ( PD ) These are devices powered by external electrical power sources. They are, for example, IP telephones and wireless Access Points or bridges. Power Source Equipment ( PSE ) These are devices supplying electrical power to other equipments. They are, for example, inline power switches and power patch panels.')
cpoePdMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 0))
cpoePdMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1))
cpoePdMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2))
cpoePdInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1))
class CpoePdPowerSourceType(TextualConvention, Integer32):
    description = 'This is the type of power source equipment supplying DC power to the PD. pending -- power source is not yet determined. acAdaptor -- power is supplied by an AC adapter thirdParty -- power is supplied by a PSE not supporting Cisco CDP classic -- power is supplied and limited by a classic Cisco PSE midspan -- power is supplied by a midspan injector cdpNegotiated -- power is negotiated using Cisco CDP highPowerClassic -- power is supplied by Cisco PSE without negotiation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("pending", 1), ("acAdaptor", 2), ("thirdParty", 3), ("classic", 4), ("midspan", 5), ("cdpNegotiated", 6), ("highPowerClassic", 7))

cpoePdCurrentPowerLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerLevel.setStatus('current')
if mibBuilder.loadTexts: cpoePdCurrentPowerLevel.setDescription('This identifies the currently how much power is consummed by the device at which this agent is running. The level shall be one of the cpoePdSupportedPowerLevel in the cpoePdSupportedPowerTable.')
cpoePdCurrentPowerSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 2), CpoePdPowerSourceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdCurrentPowerSource.setStatus('current')
if mibBuilder.loadTexts: cpoePdCurrentPowerSource.setDescription('This is the current power source type obtained from device power source detection.')
cpoePdSupportedPowerLevelTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3), )
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelTable.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelTable.setDescription('This table shows all the supported electrical power consumption levels of this agent and the corresponding modes of operation at those power levels. The mode of operation and the device capability changes as the supplied power level varies. The number of supported levels is platform and implementation dependent.')
cpoePdSupportedPowerLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-POE-PD-MIB", "cpoePdSupportedPowerLevel"))
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelEntry.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPowerLevelEntry.setDescription('Each entry shows a supported power level and the corresponding mode of operation.')
cpoePdSupportedPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cpoePdSupportedPowerLevel.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPowerLevel.setDescription('This index uniquely identifies the supported power consumption level.')
cpoePdSupportedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPower.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPower.setDescription('This is the electrical power consummed by the device operating at this supported power consumption level.')
cpoePdSupportedPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 414, 1, 1, 3, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpoePdSupportedPowerMode.setStatus('current')
if mibBuilder.loadTexts: cpoePdSupportedPowerMode.setDescription("This is a text string describing the mode of operation or capability of the device at the power consumption level. For example, the comsumption level and corresponding mode should look like these: 1 'Full power mode' 2 'Low power mode - dot11radio 0 disabled' 3 'Low power mode - dot11radio 1 disabled' 4 'Low power mode - dot11 radios disabled'.")
cpoePdMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1))
cpoePdMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2))
cpoePdMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 1, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdMIBCompliance = cpoePdMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cpoePdMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoPoePdMIB module.')
cpoePdInformationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 414, 2, 2, 1)).setObjects(("CISCO-POE-PD-MIB", "cpoePdCurrentPowerLevel"), ("CISCO-POE-PD-MIB", "cpoePdCurrentPowerSource"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPower"), ("CISCO-POE-PD-MIB", "cpoePdSupportedPowerMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpoePdInformationGroup = cpoePdInformationGroup.setStatus('current')
if mibBuilder.loadTexts: cpoePdInformationGroup.setDescription('This collection of objects provide information about the supported electrical power level, current power consumption, and mode of operation of this agent.')
mibBuilder.exportSymbols("CISCO-POE-PD-MIB", cpoePdCurrentPowerSource=cpoePdCurrentPowerSource, PYSNMP_MODULE_ID=ciscoPoePdMIB, cpoePdMIBNotifications=cpoePdMIBNotifications, cpoePdSupportedPowerLevelEntry=cpoePdSupportedPowerLevelEntry, cpoePdSupportedPower=cpoePdSupportedPower, cpoePdMIBConformance=cpoePdMIBConformance, CpoePdPowerSourceType=CpoePdPowerSourceType, cpoePdInformation=cpoePdInformation, cpoePdMIBObjects=cpoePdMIBObjects, cpoePdCurrentPowerLevel=cpoePdCurrentPowerLevel, cpoePdMIBCompliances=cpoePdMIBCompliances, cpoePdMIBCompliance=cpoePdMIBCompliance, cpoePdSupportedPowerMode=cpoePdSupportedPowerMode, ciscoPoePdMIB=ciscoPoePdMIB, cpoePdSupportedPowerLevelTable=cpoePdSupportedPowerLevelTable, cpoePdMIBGroups=cpoePdMIBGroups, cpoePdInformationGroup=cpoePdInformationGroup, cpoePdSupportedPowerLevel=cpoePdSupportedPowerLevel)
