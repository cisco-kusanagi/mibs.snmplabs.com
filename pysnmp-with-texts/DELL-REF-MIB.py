#
# PySNMP MIB module DELL-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELL-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:38:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dellLan, dellLanExtension = mibBuilder.importSymbols("Dell-Vendor-MIB", "dellLan", "dellLanExtension")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, IpAddress, Bits, NotificationType, iso, Unsigned32, Gauge32, TimeTicks, ObjectIdentity, Integer32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "IpAddress", "Bits", "NotificationType", "iso", "Unsigned32", "Gauge32", "TimeTicks", "ObjectIdentity", "Integer32", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lvl7 = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132))
lvl7.setRevisions(('2013-04-12 00:00', '2013-03-27 00:00', '2011-04-14 00:00', '2003-11-21 00:00', '2003-02-06 12:00', '2013-07-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lvl7.setRevisionsDescriptions(('Revisions made for new release.', 'Updated for new release.', 'Revisions made for new release.', 'Revisions made for new release.', 'Updated for release', 'Updated for new release',))
if mibBuilder.loadTexts: lvl7.setLastUpdated('201304120000Z')
if mibBuilder.loadTexts: lvl7.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: lvl7.setContactInfo('')
if mibBuilder.loadTexts: lvl7.setDescription('')
lvl7Products = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1))
dnOS = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1))
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

mibBuilder.exportSymbols("DELL-REF-MIB", dellN2048PSwitch=dellN2048PSwitch, dellN3024PSwitch=dellN3024PSwitch, dell6248Switch=dell6248Switch, dell7048RSwitch=dell7048RSwitch, dellM8024Switch=dellM8024Switch, dell6248PSwitch=dell6248PSwitch, dellN2048Switch=dellN2048Switch, dellN3048Switch=dellN3048Switch, dell8024FSwitch=dell8024FSwitch, dellN2024Switch=dellN2024Switch, dellM6384Switch=dellM6384Switch, dellN4064Switch=dellN4064Switch, dell7048PSwitch=dell7048PSwitch, dellN2024PSwitch=dellN2024PSwitch, lvl7=lvl7, dell7048Switch=dell7048Switch, dellN4032FSwitch=dellN4032FSwitch, dellN4064FSwitch=dellN4064FSwitch, dellN3024Switch=dellN3024Switch, dell7048RRASwitch=dell7048RRASwitch, dnOS=dnOS, dell7024Switch=dell7024Switch, dell7024PSwitch=dell7024PSwitch, dell6224PSwitch=dell6224PSwitch, dell6224FSwitch=dell6224FSwitch, dell8024Switch=dell8024Switch, dellN3048PSwitch=dellN3048PSwitch, dellN4032Switch=dellN4032Switch, dellM6220Switch=dellM6220Switch, dell6224Switch=dell6224Switch, lvl7Products=lvl7Products, dell7024FSwitch=dell7024FSwitch, dellM8024KSwitch=dellM8024KSwitch, AgentPortMask=AgentPortMask, dellN3024FSwitch=dellN3024FSwitch, PYSNMP_MODULE_ID=lvl7)
