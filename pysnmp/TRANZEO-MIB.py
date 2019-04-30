#
# PySNMP MIB module TRANZEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRANZEO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, TimeTicks, IpAddress, Bits, ObjectIdentity, Counter64, Gauge32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "Counter64", "Gauge32", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
signalaverage = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: signalaverage.setStatus('mandatory')
signalhigh = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: signalhigh.setStatus('mandatory')
noise = MibIdentifier((1, 3, 6, 1, 4, 1, 24575, 1, 2))
noiselow = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiselow.setStatus('mandatory')
noiseaverage = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiseaverage.setStatus('mandatory')
noisehigh = MibScalar((1, 3, 6, 1, 4, 1, 24575, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-110, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: noisehigh.setStatus('mandatory')
probeResetControl = MibScalar((1, 3, 6, 1, 4, 1, 24575, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("running", 1), ("warmBoot", 2), ("coldBoot", 3), ("autoconfig", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: probeResetControl.setStatus('mandatory')
stnNumber = MibScalar((1, 3, 6, 1, 4, 1, 24575, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnNumber.setStatus('mandatory')
stnIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 24575, 4, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnIpAddr.setStatus('mandatory')
stnMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 24575, 4, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnMacAddr.setStatus('deprecated')
mibBuilder.exportSymbols("TRANZEO-MIB", signalhigh=signalhigh, stationStat=stationStat, probeConfig=probeConfig, PhysAddress=PhysAddress, noiseaverage=noiseaverage, noise=noise, noisehigh=noisehigh, stnNumber=stnNumber, stnMacAddr=stnMacAddr, probeResetControl=probeResetControl, assocStation=assocStation, signalaverage=signalaverage, rssi=rssi, signallow=signallow, signal=signal, stnIpAddr=stnIpAddr, tranzeo=tranzeo, noiselow=noiselow)
