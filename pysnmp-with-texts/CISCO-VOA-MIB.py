#
# PySNMP MIB module CISCO-VOA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
OpticalIfDirection, = mibBuilder.importSymbols("CISCO-OPTICAL-MONITOR-MIB", "OpticalIfDirection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, NotificationType, IpAddress, Bits, Integer32, MibIdentifier, TimeTicks, Gauge32, ObjectIdentity, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "IpAddress", "Bits", "Integer32", "MibIdentifier", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64")
TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString")
ciscoVoaMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 262))
ciscoVoaMIB.setRevisions(('2002-05-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoaMIB.setRevisionsDescriptions(('The initial revision of this MIB.',))
if mibBuilder.loadTexts: ciscoVoaMIB.setLastUpdated('200205070000Z')
if mibBuilder.loadTexts: ciscoVoaMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoaMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-dwdm@cisco.com')
if mibBuilder.loadTexts: ciscoVoaMIB.setDescription('This MIB module defines objects to configure and manage the Variable Optical Attenuator (VOA) modules. VOA modules are typically used to attenuate channels added by a network element, in order to equalize the input power of each wavelength before the multiplexed signal consisting of all wavelengths is sent through an EDFA. There may be a separate VOA per channel, one VOA per band of wavelengths, or one VOA for the pass through wavelengths. VOA modules are also often used before terminating optical wavelengths at optical receivers, in order to avoid receiver saturation. The VOAs may be present on various modules within the network element, for example, on an Optical Add/Drop Multiplexer (OADM) module, on the same module as an optical transceiver, or on a separate module of its own. ')
class OpticalPowerInDbm(TextualConvention, Integer32):
    description = "An integer value that gives the optical power level in 1/10ths of dBm. Example: The value -300 represents a power level of -30.0 dBm. The distinguished value of '-1000' indicates that the object has not yet been initialized. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-400, 250), ValueRangeConstraint(-1000, -1000), )
class OpticalAttenInDb(TextualConvention, Integer32):
    description = 'An integer value that gives the attenuation level in 1/10ths of dB. Example: The value 80 represents an attenuation level of 8.0 dB. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 400)

cVoaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 1))
cVoaBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1))
cVoaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1), )
if mibBuilder.loadTexts: cVoaTable.setStatus('current')
if mibBuilder.loadTexts: cVoaTable.setDescription('This table provides objects to configure and control the attenuation on VOAs.')
cVoaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-VOA-MIB", "cVoaDirection"))
if mibBuilder.loadTexts: cVoaEntry.setStatus('current')
if mibBuilder.loadTexts: cVoaEntry.setDescription('An entry in the cVoaTable provides objects to configure and control the attenuation level of a VOA at an interface, for a given direction.')
cVoaDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 1), OpticalIfDirection())
if mibBuilder.loadTexts: cVoaDirection.setStatus('current')
if mibBuilder.loadTexts: cVoaDirection.setDescription('This is the second index into the cVoaTable and indicates the direction for which the attenuation level at this interface is being controlled, in this entry.')
cVoaAttenuationControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("automatic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaAttenuationControlMode.setStatus('current')
if mibBuilder.loadTexts: cVoaAttenuationControlMode.setDescription("This object is used to set the mode of controlling the attenuation level of a VOA at an interface. When the mode is set to 'manual', the attenuation level is configured manually, by setting the desired attenuation level in the cVoaAttenuation object. The cVoaDesiredPower object does not apply in this case. When the mode is set to 'automatic', the attenuation level is continuously adjusted to maintain a desired power level, after attenuation. The desired optical power level after attenuation is configured using the cVoaDesiredPower object. The cVoaAttenuation object cannot be configured in this case, but it indicates the attenuation level derived from the desired power level. The automatic mode of controlling attenuation should not be used when the monitored power level includes multiple wavelengths, since the power level monitor cannot distinguish between a decrease in power across all wavelengths, versus a loss of power of some but not all wavelengths. If some but not all wavelengths go down, this would cause the attenuation level to be automatically decreased, leading to an increase in the power level of the remaining wavelengths.")
cVoaAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 3), OpticalAttenInDb()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaAttenuation.setStatus('current')
if mibBuilder.loadTexts: cVoaAttenuation.setDescription("This object indicates the attenuation level applied at the interface. When the cVoaAttenuationControlMode object is set to 'manual', the attenuation level may be specified by setting this object.")
cVoaAttenuationLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVoaAttenuationLastChange.setStatus('current')
if mibBuilder.loadTexts: cVoaAttenuationLastChange.setDescription('This object indicates the value of sysUpTime at the last time the attenuation level was adjusted at this interface, in the given direction.')
cVoaDesiredPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 262, 1, 1, 1, 1, 5), OpticalPowerInDbm()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoaDesiredPower.setStatus('current')
if mibBuilder.loadTexts: cVoaDesiredPower.setDescription("This object indicates the desired optical power level, after attenuation, at the interface. This object applies only when the cVoaAttenuationControlMode object is set to 'automatic'. In this mode, the attenuation level is continuously adjusted to maintain the desired power level, after attenuation, as specified by this object.")
cVoaMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3))
cVoaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1))
cVoaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2))
cVoaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 1, 1)).setObjects(("CISCO-VOA-MIB", "cVoaMIBBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoaMIBCompliance = cVoaMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cVoaMIBCompliance.setDescription('The compliance statement for platforms that provide configuration and control of VOA modules.')
cVoaMIBBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 262, 3, 2, 1)).setObjects(("CISCO-VOA-MIB", "cVoaAttenuationControlMode"), ("CISCO-VOA-MIB", "cVoaAttenuation"), ("CISCO-VOA-MIB", "cVoaAttenuationLastChange"), ("CISCO-VOA-MIB", "cVoaDesiredPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoaMIBBaseGroup = cVoaMIBBaseGroup.setStatus('current')
if mibBuilder.loadTexts: cVoaMIBBaseGroup.setDescription('A collection of mandatory managed objects that provide basic configuration and control of the VOA modules.')
mibBuilder.exportSymbols("CISCO-VOA-MIB", cVoaMIBGroups=cVoaMIBGroups, cVoaAttenuationLastChange=cVoaAttenuationLastChange, cVoaMIBBaseGroup=cVoaMIBBaseGroup, cVoaDesiredPower=cVoaDesiredPower, ciscoVoaMIB=ciscoVoaMIB, cVoaMIBConformance=cVoaMIBConformance, cVoaMIBCompliance=cVoaMIBCompliance, OpticalAttenInDb=OpticalAttenInDb, PYSNMP_MODULE_ID=ciscoVoaMIB, cVoaBaseGroup=cVoaBaseGroup, cVoaMIBCompliances=cVoaMIBCompliances, cVoaDirection=cVoaDirection, cVoaEntry=cVoaEntry, cVoaAttenuation=cVoaAttenuation, cVoaAttenuationControlMode=cVoaAttenuationControlMode, OpticalPowerInDbm=OpticalPowerInDbm, cVoaTable=cVoaTable, cVoaMIBObjects=cVoaMIBObjects)
