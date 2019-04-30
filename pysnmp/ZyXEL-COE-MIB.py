#
# PySNMP MIB module ZyXEL-COE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZyXEL-COE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:46:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, Unsigned32, Bits, ModuleIdentity, iso, NotificationType, TimeTicks, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, enterprises, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "Unsigned32", "Bits", "ModuleIdentity", "iso", "NotificationType", "TimeTicks", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "enterprises", "ObjectIdentity", "MibIdentifier")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

zyxel = MibIdentifier((1, 3, 6, 1, 4, 1, 890))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1))
prestige = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 2))
mtu = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3))
dslam = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4))
systemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 999))
aes_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 1)).setLabel("aes-100")
pes_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 2)).setLabel("pes-100")
ves_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 3)).setLabel("ves-100")
shes_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 4)).setLabel("shes-100")
p1600 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 5))
p1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 6))
p2100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 7))
aes_100_1 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 3, 8)).setLabel("aes-100-1")
zysam_1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4, 1)).setLabel("zysam-1000")
zysam_1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4, 2)).setLabel("zysam-1100")
zysam_1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4, 3)).setLabel("zysam-1200")
zysam_2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 4, 4)).setLabel("zysam-2000")
problemCause = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 999, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: problemCause.setStatus('mandatory')
systemTemperature = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 999, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemTemperature.setStatus('mandatory')
reboot = NotificationType((1, 3, 6, 1, 4, 1, 890) + (0,1)).setObjects(("ZyXEL-COE-MIB", "problemCause"))
systemShutdown = NotificationType((1, 3, 6, 1, 4, 1, 890) + (0,2)).setObjects(("ZyXEL-COE-MIB", "problemCause"))
overheat = NotificationType((1, 3, 6, 1, 4, 1, 890) + (0,3)).setObjects(("ZyXEL-COE-MIB", "systemTemperature"))
overheatOver = NotificationType((1, 3, 6, 1, 4, 1, 890) + (0,4)).setObjects(("ZyXEL-COE-MIB", "systemTemperature"))
mibBuilder.exportSymbols("ZyXEL-COE-MIB", reboot=reboot, pes_100=pes_100, p1600=p1600, products=products, shes_100=shes_100, overheat=overheat, zysam_1200=zysam_1200, p2100=p2100, aes_100_1=aes_100_1, problemCause=problemCause, zyxel=zyxel, mtu=mtu, systemShutdown=systemShutdown, aes_100=aes_100, systemTraps=systemTraps, ves_100=ves_100, prestige=prestige, zysam_1100=zysam_1100, overheatOver=overheatOver, zysam_2000=zysam_2000, zysam_1000=zysam_1000, DisplayString=DisplayString, systemTemperature=systemTemperature, dslam=dslam, p1400=p1400)
