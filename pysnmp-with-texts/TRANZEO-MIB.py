#
# PySNMP MIB module TRANZEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRANZEO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, TimeTicks, Gauge32, ObjectIdentity, Counter64, iso, ModuleIdentity, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter64", "iso", "ModuleIdentity", "Counter32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PhysAddress(OctetString):
    pass

tranzeo = MibIdentifier((1, 3, 6, 1, 4, 1, 24575))
signal = MibIdentifier((1, 3, 6, 1, 4, 1, 24575, 1))
probeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 24575, 2))
stationStat = MibIdentifier((1, 3, 6, 1, 4, 1, 24575, 3))
assocStation = MibIdentifier((1, 3, 6, 1, 4, 1, 24575, 4))
rssi = MibIdentifier((1, 3, 6, 1, 4, 1, 24575, 1, 1))
signallow = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: signallow.setStatus('mandatory')
if mibBuilder.loadTexts: signallow.setDescription('This object represents the lowest received signal strength on the current channel in dBm. A 0 means no wireless connection.')
signalaverage = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: signalaverage.setStatus('mandatory')
if mibBuilder.loadTexts: signalaverage.setDescription('This object represents the average received signal strength on the current channel in dBm. A 0 means no wireless connection.')
signalhigh = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: signalhigh.setStatus('mandatory')
if mibBuilder.loadTexts: signalhigh.setDescription('This object represents the highest received signal strength on the current channel in dBm. A 0 means no wireless connection.')
noise = MibIdentifier((1, 3, 6, 1, 4, 1, 24575, 1, 2))
noiselow = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiselow.setStatus('mandatory')
if mibBuilder.loadTexts: noiselow.setDescription('This object represents the lowest noise on the current channel in dBm. A 0 means no wireless connection.')
noiseaverage = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiseaverage.setStatus('mandatory')
if mibBuilder.loadTexts: noiseaverage.setDescription('This object represents the average noise on the current channel in dBm. A 0 means no wireless connection.')
noisehigh = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noisehigh.setStatus('mandatory')
if mibBuilder.loadTexts: noisehigh.setDescription('This object represents the highest noise on the current channel in dBm. A 0 means no wireless connection.')
probeResetControl = MibScalar((1, 3, 6, 1, 4, 1, 24575, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("running", 1), ("warmBoot", 2), ("coldBoot", 3), ("autoconfig", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: probeResetControl.setStatus('mandatory')
if mibBuilder.loadTexts: probeResetControl.setDescription('Setting this object to warmBoot(2) causes the device to restart the application software with current configuration parameters saved in non-volatile memory. Setting this object to coldBoot(3) causes the device to reinitialize configuration parameters in non-volatile memory to default values and restart the application software. When the device is running normally, this variable has a value of running(1). Setting this object to autoconfig(4) causes the device to reboot and download the configuration using TFTP.')
stnNumber = MibScalar((1, 3, 6, 1, 4, 1, 24575, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnNumber.setStatus('mandatory')
if mibBuilder.loadTexts: stnNumber.setDescription('This object represents the number of stations that associates to this AP.')
stnIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 24575, 4, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIpAddr.setStatus('mandatory')
if mibBuilder.loadTexts: stnIpAddr.setDescription('This object represents the ip address of associated STN to this AP.')
stnMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 24575, 4, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnMacAddr.setStatus('deprecated')
if mibBuilder.loadTexts: stnMacAddr.setDescription('This object represents the MAC address of associated STN to this AP.')
mibBuilder.exportSymbols("TRANZEO-MIB", probeResetControl=probeResetControl, signallow=signallow, PhysAddress=PhysAddress, stationStat=stationStat, probeConfig=probeConfig, assocStation=assocStation, stnNumber=stnNumber, signal=signal, tranzeo=tranzeo, noise=noise, stnIpAddr=stnIpAddr, noiselow=noiselow, signalaverage=signalaverage, rssi=rssi, stnMacAddr=stnMacAddr, noiseaverage=noiseaverage, noisehigh=noisehigh, signalhigh=signalhigh)
