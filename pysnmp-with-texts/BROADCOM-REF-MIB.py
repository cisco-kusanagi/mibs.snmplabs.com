#
# PySNMP MIB module BROADCOM-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROADCOM-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:40:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dellLanExtension, dellLan = mibBuilder.importSymbols("Dell-Vendor-MIB", "dellLanExtension", "dellLan")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, MibIdentifier, ModuleIdentity, Bits, Unsigned32, IpAddress, Gauge32, NotificationType, iso, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Bits", "Unsigned32", "IpAddress", "Gauge32", "NotificationType", "iso", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lvl7 = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132))
lvl7.setRevisions(('2013-04-12 00:00', '2013-03-27 00:00', '2011-04-14 00:00', '2003-11-21 00:00', '2003-02-06 12:00', '2013-07-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lvl7.setRevisionsDescriptions(('Revisions made for new release.', 'Updated for new release.', 'Revisions made for new release.', 'Revisions made for new release.', 'Updated for release', 'Updated for new release',))
if mibBuilder.loadTexts: lvl7.setLastUpdated('201304120000Z')
if mibBuilder.loadTexts: lvl7.setOrganization('Broadcom Corporation')
if mibBuilder.loadTexts: lvl7.setContactInfo(' Customer Support Postal: Broadcom Corporation 100, Perimeter Park Drive Morrisville, NC 27560 Tel: +1 919 865 2700')
if mibBuilder.loadTexts: lvl7.setDescription('')
lvl7Products = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1))
fastPath = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1))
dell6224Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3010))
dell6248Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3011))
dell6224PSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3012))
dell6248PSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3013))
dell6224FSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3014))
dellM6220Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3015))
dellM8024Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3022))
dell8024Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3023))
dell8024FSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3024))
dellM6384Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3025))
dell7024Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3034))
dell7048Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3035))
dell7024PSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3036))
dell7048PSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3037))
dell7024FSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3038))
dell7048RSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3039))
dell7048RRASwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3040))
dellM8024KSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3041))
dellN4032Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3042))
dellN4032FSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3044))
dellN4064Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3045))
dellN4064FSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3046))
dellN2024Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3053))
dellN2048Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3054))
dellN2024PSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3055))
dellN2048PSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3056))
dellN3024Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3057))
dellN3048Switch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3058))
dellN3024PSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3059))
dellN3048PSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3060))
dellN3024FSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 3061))
class AgentPortMask(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port. Thus, each port of the bridge is represented by a single bit within the value of this object. If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0' When setting this value, the system will ignore configuration for ports not between the first and last valid ports. Configuration of any port numbers between this range that are not valid ports return a failure message, but will still apply configuration for valid ports."
    status = 'current'
    displayHint = '255x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

mibBuilder.exportSymbols("BROADCOM-REF-MIB", dell6248PSwitch=dell6248PSwitch, dell7048PSwitch=dell7048PSwitch, dell7048Switch=dell7048Switch, dellN2024Switch=dellN2024Switch, lvl7Products=lvl7Products, dellN3048PSwitch=dellN3048PSwitch, fastPath=fastPath, dellN4032FSwitch=dellN4032FSwitch, dellN2024PSwitch=dellN2024PSwitch, dell6224FSwitch=dell6224FSwitch, dellN3024FSwitch=dellN3024FSwitch, dell7024Switch=dell7024Switch, dellN3048Switch=dellN3048Switch, dellM8024KSwitch=dellM8024KSwitch, dell7024FSwitch=dell7024FSwitch, dellN4064Switch=dellN4064Switch, dell8024Switch=dell8024Switch, dellN2048PSwitch=dellN2048PSwitch, dellN4064FSwitch=dellN4064FSwitch, PYSNMP_MODULE_ID=lvl7, dell7048RSwitch=dell7048RSwitch, dellN2048Switch=dellN2048Switch, dell6248Switch=dell6248Switch, dell6224PSwitch=dell6224PSwitch, dell7024PSwitch=dell7024PSwitch, dellM6220Switch=dellM6220Switch, dellN4032Switch=dellN4032Switch, AgentPortMask=AgentPortMask, lvl7=lvl7, dellM6384Switch=dellM6384Switch, dell6224Switch=dell6224Switch, dellN3024Switch=dellN3024Switch, dell7048RRASwitch=dell7048RRASwitch, dellN3024PSwitch=dellN3024PSwitch, dell8024FSwitch=dell8024FSwitch, dellM8024Switch=dellM8024Switch)
