#
# PySNMP MIB module PACKETFLUX-STANDBYPOWER (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PACKETFLUX-STANDBYPOWER
# Produced by pysmi-0.3.4 at Wed May  1 14:36:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
packetfluxMgmt, = mibBuilder.importSymbols("PACKETFLUX-SMI", "packetfluxMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, ObjectIdentity, TimeTicks, Counter32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, iso, ModuleIdentity, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ObjectIdentity", "TimeTicks", "Counter32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "iso", "ModuleIdentity", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
standbypower = ModuleIdentity((1, 3, 6, 1, 4, 1, 32050, 2, 2))
standbypower.setRevisions(('2013-06-04 16:49',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: standbypower.setRevisionsDescriptions(('initial version of this module',))
if mibBuilder.loadTexts: standbypower.setLastUpdated('201306041649Z')
if mibBuilder.loadTexts: standbypower.setOrganization('PacketFlux Technologies')
if mibBuilder.loadTexts: standbypower.setContactInfo('custsvc@packetflux.com http://www.packetflux.com')
if mibBuilder.loadTexts: standbypower.setDescription('MIB for the PacketFlux Standby Power Controller')
powercontrollerstate = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("onprimarypower", 1), ("startingstandby", 2), ("transferringtostandby", 3), ("onstandbypower", 4), ("transferringtoprimary", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powercontrollerstate.setStatus('current')
if mibBuilder.loadTexts: powercontrollerstate.setDescription('The status of the standby power controller.')
transferswitchstate = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("primary", 1), ("transfertostandby1", 2), ("transfertostandby2", 3), ("transfertostandby3", 4), ("standby", 5), ("transfertoprimary1", 6), ("transfertoprimary2", 7), ("transfertoprimary3", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transferswitchstate.setStatus('current')
if mibBuilder.loadTexts: transferswitchstate.setDescription('The current state in the transfer sequence.')
standbypowerstate = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))).clone(namedValues=NamedValues(("stopped", 1), ("prepare1", 2), ("prepare2", 3), ("prepare3", 4), ("startup1", 5), ("startup2", 6), ("startup3", 7), ("checkrun", 8), ("reprepare1", 9), ("reprepare2", 10), ("reprepare3", 11), ("warmup1", 12), ("warmup2", 13), ("warmup3", 14), ("verifyrun", 15), ("running", 16), ("cooldown1", 17), ("cooldown2", 18), ("cooldown3", 19), ("shutdown1", 20), ("shutdown2", 21), ("shutdown3", 22), ("verifystopped", 23), ("postshutdown1", 24), ("postshutdown2", 25), ("postshutdown3", 26)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: standbypowerstate.setStatus('current')
if mibBuilder.loadTexts: standbypowerstate.setDescription('The current state in the standby power sequence.')
ac1voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ac1voltage.setStatus('current')
if mibBuilder.loadTexts: ac1voltage.setDescription('The voltage of the AC input AC1 in 1/10ths of a volt.')
ac1frequency = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ac1frequency.setStatus('current')
if mibBuilder.loadTexts: ac1frequency.setDescription('The frequency of the AC input AC1 in 1/100ths of a Hertz.')
ac2voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ac2voltage.setStatus('current')
if mibBuilder.loadTexts: ac2voltage.setDescription('The voltage of the AC input AC2 in 1/10ths of a volt.')
ac2frequency = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ac2frequency.setStatus('current')
if mibBuilder.loadTexts: ac2frequency.setDescription('The frequency of the AC input AC2 in 1/100ths of a Hertz.')
mtr1voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtr1voltage.setStatus('current')
if mibBuilder.loadTexts: mtr1voltage.setDescription('The voltage of the DC input Mtr1 in 1/10ths of a volt.')
mtr2voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtr2voltage.setStatus('current')
if mibBuilder.loadTexts: mtr2voltage.setDescription('The voltage of the DC input Mtr2 in 1/10ths of a volt.')
pwr1voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwr1voltage.setStatus('current')
if mibBuilder.loadTexts: pwr1voltage.setDescription('The voltage of the DC input Pwr3 in 1/10ths of a volt.')
pwr2voltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pwr2voltage.setStatus('current')
if mibBuilder.loadTexts: pwr2voltage.setDescription('The voltage of the DC input Pwr2 in 1/10ths of a volt.')
shuntvoltage = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: shuntvoltage.setStatus('current')
if mibBuilder.loadTexts: shuntvoltage.setDescription('The voltage of the DC input Shunt in 1/10ths of a millivolt. Can be negative.')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
if mibBuilder.loadTexts: temperature.setDescription('The temperature of the onboard temperature sensor in 1/10ths of a degree centigrade.')
recentunsuccessfulstarts = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: recentunsuccessfulstarts.setStatus('current')
if mibBuilder.loadTexts: recentunsuccessfulstarts.setDescription('The number of times the standby power source was not successfully started. This counter resets upon a successful start. It can also be reset via the web interface or by writing 0 to this object.')
totalunsuccessfulstarts = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totalunsuccessfulstarts.setStatus('current')
if mibBuilder.loadTexts: totalunsuccessfulstarts.setDescription('The number of times the standby power source was not successfully started. This counter DOES NOT reset upon a successful start. It can be reset via the web interface or by writing 0 to this object.')
recentstalls = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: recentstalls.setStatus('current')
if mibBuilder.loadTexts: recentstalls.setDescription('The number of times the standby power source has stalled. This counter resets upon a clean shutdown. It can also be reset via the web interface or by writing 0 to this object.')
totalstalls = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totalstalls.setStatus('current')
if mibBuilder.loadTexts: totalstalls.setDescription('The number of times the standby power source has stalled. This counter DOES NOT reset upon a clean shutdown. It can be reset via the web interface or by writing 0 to this object.')
numberofstarts = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberofstarts.setStatus('current')
if mibBuilder.loadTexts: numberofstarts.setDescription('The number of times the secondary power source has started. This counter increments when the standby sequence reaches the running state. This counter can be reset via the web interface or by writing 0 to this object.')
numberoftransfers = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberoftransfers.setStatus('current')
if mibBuilder.loadTexts: numberoftransfers.setDescription('The number of times the power has transfered from primary to standby, or back. A complete transfer cycle from primary to standby and back to primary will increment this counter twice. This counter can be reset via the web interface or by writing 0 to this object.')
currenttimeonprimary = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 20), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currenttimeonprimary.setStatus('current')
if mibBuilder.loadTexts: currenttimeonprimary.setDescription('The amount of time the transfer switch has been in the primary state (position) since the most recent transfer to that state. This timer resets to zero when the transfer switch leaves the primary state (position). This timer can be reset via the web interface or by writing 0 to this object.')
totaltimeonprimary = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 21), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totaltimeonprimary.setStatus('current')
if mibBuilder.loadTexts: totaltimeonprimary.setDescription('The amount of time the transfer switch has been in the primary state (position) since power on or the last reset of this counter. This timer does not automatically reset. This timer can be reset via the web interface or by writing 0 to this object.')
currenttimeonstandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 22), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currenttimeonstandby.setStatus('current')
if mibBuilder.loadTexts: currenttimeonstandby.setDescription('The amount of time the transfer switch has been in the standby state (position) since the most recent transfer to that state. This timer resets to zero when the transfer switch leaves the primary state (position). This timer can be reset via the web interface or by writing 0 to this object.')
totaltimeonstandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 23), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totaltimeonstandby.setStatus('current')
if mibBuilder.loadTexts: totaltimeonstandby.setDescription('The amount of time the transfer switch has been in the standby state (position) since power on or the last reset of this counter. This timer does not automatically reset. This timer can be reset via the web interface or by writing 0 to this object.')
currentstandbyruntime = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 24), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: currentstandbyruntime.setStatus('current')
if mibBuilder.loadTexts: currentstandbyruntime.setDescription("The amount of time the standby power source has been running during it's current run. This timer resets to zero when the standby power source shuts down. This timer can be reset via the web interface or by writing 0 to this object.")
totalstandbyruntime = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 25), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: totalstandbyruntime.setStatus('current')
if mibBuilder.loadTexts: totalstandbyruntime.setDescription('The amount of time the standby power source has been running since power on or the last reset of this counter. This timer does not automatically reset. This timer can be reset via the web interface or by writing 0 to this object.')
laststandbyrun = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 26), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laststandbyrun.setStatus('current')
if mibBuilder.loadTexts: laststandbyrun.setDescription('The amount of time since the standby power source ran last. This timer resets upon start of the standby power source and starts timing upon shutdown of the standby power source. This timer can be reset via the web interface or by writing 0 to this object.')
laststandbygracefulstop = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 27), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laststandbygracefulstop.setStatus('current')
if mibBuilder.loadTexts: laststandbygracefulstop.setDescription('The amount of time since standby power source was gracefully shutdown. This timer resets and starts timing upon graceful shutdown of the standby power source. This timer can be reset via the web interface or by writing 0 to this object.')
laststandbyunsuccessfulstart = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 28), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laststandbyunsuccessfulstart.setStatus('current')
if mibBuilder.loadTexts: laststandbyunsuccessfulstart.setDescription('The amount of time since the last failed start of the standby power source . This timer resets and starts timing upon a unsuccessful start of the power source. This timer can be reset via the web interface or by writing 0 to this object.')
laststandbyfailure = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 29), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laststandbyfailure.setStatus('current')
if mibBuilder.loadTexts: laststandbyfailure.setDescription('The amount of time since the stall or failure while running of the standby power source . This timer resets and starts timing upon a stall/failure of the power source. This timer can be reset via the web interface or by writing 0 to this object.')
switch1closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 30), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch1closed.setStatus('current')
if mibBuilder.loadTexts: switch1closed.setDescription('True(1) if the Switch 1 input is closed (shorted/on). False(2) if it is open.')
switch2closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 31), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch2closed.setStatus('current')
if mibBuilder.loadTexts: switch2closed.setDescription('True(1) if the Switch 2 input is closed (shorted/on). False(2) if it is open.')
switch3closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 32), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch3closed.setStatus('current')
if mibBuilder.loadTexts: switch3closed.setDescription('True(1) if the Switch 3 input is closed (shorted/on). False(2) if it is open.')
switch4closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 33), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch4closed.setStatus('current')
if mibBuilder.loadTexts: switch4closed.setDescription('True(1) if the Switch 4 input is closed (shorted/on). False(2) if it is open.')
switch5closed = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 34), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switch5closed.setStatus('current')
if mibBuilder.loadTexts: switch5closed.setDescription('True(1) if the Switch 5 input is closed (shorted/on). False(2) if it is open.')
enabled = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 35), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: enabled.setStatus('current')
if mibBuilder.loadTexts: enabled.setDescription('True(1) if the enable input is closed (shorted/on). False(2) if it is open.')
relay1on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 36), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay1on.setStatus('current')
if mibBuilder.loadTexts: relay1on.setDescription('True(1) if the Relay 1 ouput is on (C and NO connected). False(2) if it is off (C and NC connected).')
relay2on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 37), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay2on.setStatus('current')
if mibBuilder.loadTexts: relay2on.setDescription('True(1) if the Relay 2 ouput is on (C and NO connected). False(2) if it is off (C and NC connected).')
relay3on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 38), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay3on.setStatus('current')
if mibBuilder.loadTexts: relay3on.setDescription('True(1) if the Relay 3 ouput is on (C and NO connected). False(2) if it is off (C and NC connected).')
relay4on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 39), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay4on.setStatus('current')
if mibBuilder.loadTexts: relay4on.setDescription('True(1) if the Relay 4 ouput is on (C and NO connected). False(2) if it is off (C and NC connected).')
relay5on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 40), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay5on.setStatus('current')
if mibBuilder.loadTexts: relay5on.setDescription('True(1) if the Relay 5 output is on (C and NO connected). False(2) if it is off (C and NC connected).')
relay6on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 41), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay6on.setStatus('current')
if mibBuilder.loadTexts: relay6on.setDescription('True(1) if the Relay 6 output is on (C and NO connected). False(2) if it is off (C and NC connected).')
relay7on = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 42), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: relay7on.setStatus('current')
if mibBuilder.loadTexts: relay7on.setDescription('True(1) if the Relay 7 output is on (C and NO connected). False(2) if it is off (C and NC connected).')
ruleswitchstandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 43), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruleswitchstandby.setStatus('current')
if mibBuilder.loadTexts: ruleswitchstandby.setDescription('True(1) if the switch to standby rule is true. False(2) if it is not.')
rulereturnprimary = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 44), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rulereturnprimary.setStatus('current')
if mibBuilder.loadTexts: rulereturnprimary.setDescription('True(1) if the return to primary rule is true. False(2) if it is not.')
rulestandbygood = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 45), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rulestandbygood.setStatus('current')
if mibBuilder.loadTexts: rulestandbygood.setDescription('True(1) if the standby power good rule is true. False(2) if it is not.')
rulestopstandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 46), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rulestopstandby.setStatus('current')
if mibBuilder.loadTexts: rulestopstandby.setDescription('True(1) if the stop standby and consider it failed rule is true. False(2) if it is not.')
ruleexercisestandby = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 47), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruleexercisestandby.setStatus('current')
if mibBuilder.loadTexts: ruleexercisestandby.setDescription('True(1) if the exercise standby without transfer rule is true. False(2) if it is not.')
webcontrol1 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 48), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol1.setStatus('current')
if mibBuilder.loadTexts: webcontrol1.setDescription('True(1) if the webcontrol 1 virtual toggle switch is in the on position. False(2) if it is not. This value can be written to affect the position of the toggle switch.')
webcontrol2 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 49), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol2.setStatus('current')
if mibBuilder.loadTexts: webcontrol2.setDescription('True(1) if the webcontrol 2 virtual toggle switch is in the on position. False(2) if it is not. This value can be written to affect the position of the toggle switch.')
webcontrol3 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 50), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol3.setStatus('current')
if mibBuilder.loadTexts: webcontrol3.setDescription('True(1) if the webcontrol 3 virtual toggle switch is in the on position. False(2) if it is not. This value can be written to affect the position of the toggle switch.')
webcontrol4 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 51), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol4.setStatus('current')
if mibBuilder.loadTexts: webcontrol4.setDescription('True(1) if the webcontrol 4 virtual toggle switch is in the on position. False(2) if it is not. This value can be written to affect the position of the toggle switch.')
webcontrol5 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 52), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol5.setStatus('current')
if mibBuilder.loadTexts: webcontrol5.setDescription('True(1) if the webcontrol 5 virtual toggle switch is in the on position. False(2) if it is not. This value can be written to affect the position of the toggle switch.')
webcontrol6 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 53), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol6.setStatus('current')
if mibBuilder.loadTexts: webcontrol6.setDescription('True(1) if the webcontrol 6 virtual toggle switch is in the on position. False(2) if it is not. This value can be written to affect the position of the toggle switch.')
webcontrol7 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 54), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol7.setStatus('current')
if mibBuilder.loadTexts: webcontrol7.setDescription('True(1) if the webcontrol 7 virtual toggle switch is in the on position. False(2) if it is not. This value can be written to affect the position of the toggle switch.')
webcontrol8 = MibScalar((1, 3, 6, 1, 4, 1, 32050, 2, 2, 55), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: webcontrol8.setStatus('current')
if mibBuilder.loadTexts: webcontrol8.setDescription('True(1) if the webcontrol 8 virtual toggle switch is in the on position. False(2) if it is not. This value can be written to affect the position of the toggle switch.')
standbypowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 32050, 2, 2, 256))
standbypowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 32050, 2, 2, 256, 1))
packetfluxStandbypowerAllObjects = ObjectGroup((1, 3, 6, 1, 4, 1, 32050, 2, 2, 256, 1, 1)).setObjects(("PACKETFLUX-STANDBYPOWER", "powercontrollerstate"), ("PACKETFLUX-STANDBYPOWER", "transferswitchstate"), ("PACKETFLUX-STANDBYPOWER", "standbypowerstate"), ("PACKETFLUX-STANDBYPOWER", "ac1voltage"), ("PACKETFLUX-STANDBYPOWER", "ac1frequency"), ("PACKETFLUX-STANDBYPOWER", "ac2voltage"), ("PACKETFLUX-STANDBYPOWER", "ac2frequency"), ("PACKETFLUX-STANDBYPOWER", "mtr1voltage"), ("PACKETFLUX-STANDBYPOWER", "mtr2voltage"), ("PACKETFLUX-STANDBYPOWER", "pwr1voltage"), ("PACKETFLUX-STANDBYPOWER", "pwr2voltage"), ("PACKETFLUX-STANDBYPOWER", "shuntvoltage"), ("PACKETFLUX-STANDBYPOWER", "temperature"), ("PACKETFLUX-STANDBYPOWER", "recentunsuccessfulstarts"), ("PACKETFLUX-STANDBYPOWER", "totalunsuccessfulstarts"), ("PACKETFLUX-STANDBYPOWER", "recentstalls"), ("PACKETFLUX-STANDBYPOWER", "totalstalls"), ("PACKETFLUX-STANDBYPOWER", "numberofstarts"), ("PACKETFLUX-STANDBYPOWER", "numberoftransfers"), ("PACKETFLUX-STANDBYPOWER", "currenttimeonprimary"), ("PACKETFLUX-STANDBYPOWER", "totaltimeonprimary"), ("PACKETFLUX-STANDBYPOWER", "currenttimeonstandby"), ("PACKETFLUX-STANDBYPOWER", "totaltimeonstandby"), ("PACKETFLUX-STANDBYPOWER", "currentstandbyruntime"), ("PACKETFLUX-STANDBYPOWER", "totalstandbyruntime"), ("PACKETFLUX-STANDBYPOWER", "laststandbyrun"), ("PACKETFLUX-STANDBYPOWER", "laststandbygracefulstop"), ("PACKETFLUX-STANDBYPOWER", "laststandbyunsuccessfulstart"), ("PACKETFLUX-STANDBYPOWER", "laststandbyfailure"), ("PACKETFLUX-STANDBYPOWER", "switch1closed"), ("PACKETFLUX-STANDBYPOWER", "switch2closed"), ("PACKETFLUX-STANDBYPOWER", "switch3closed"), ("PACKETFLUX-STANDBYPOWER", "switch4closed"), ("PACKETFLUX-STANDBYPOWER", "switch5closed"), ("PACKETFLUX-STANDBYPOWER", "enabled"), ("PACKETFLUX-STANDBYPOWER", "relay1on"), ("PACKETFLUX-STANDBYPOWER", "relay2on"), ("PACKETFLUX-STANDBYPOWER", "relay3on"), ("PACKETFLUX-STANDBYPOWER", "relay4on"), ("PACKETFLUX-STANDBYPOWER", "relay5on"), ("PACKETFLUX-STANDBYPOWER", "relay6on"), ("PACKETFLUX-STANDBYPOWER", "relay7on"), ("PACKETFLUX-STANDBYPOWER", "ruleswitchstandby"), ("PACKETFLUX-STANDBYPOWER", "rulereturnprimary"), ("PACKETFLUX-STANDBYPOWER", "rulestandbygood"), ("PACKETFLUX-STANDBYPOWER", "rulestopstandby"), ("PACKETFLUX-STANDBYPOWER", "ruleexercisestandby"), ("PACKETFLUX-STANDBYPOWER", "webcontrol1"), ("PACKETFLUX-STANDBYPOWER", "webcontrol2"), ("PACKETFLUX-STANDBYPOWER", "webcontrol3"), ("PACKETFLUX-STANDBYPOWER", "webcontrol4"), ("PACKETFLUX-STANDBYPOWER", "webcontrol5"), ("PACKETFLUX-STANDBYPOWER", "webcontrol6"), ("PACKETFLUX-STANDBYPOWER", "webcontrol7"), ("PACKETFLUX-STANDBYPOWER", "webcontrol8"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    packetfluxStandbypowerAllObjects = packetfluxStandbypowerAllObjects.setStatus('current')
if mibBuilder.loadTexts: packetfluxStandbypowerAllObjects.setDescription('This automatically created object group contains all those objects that do not belong to any other OBJECT-GROUP')
mibBuilder.exportSymbols("PACKETFLUX-STANDBYPOWER", rulestopstandby=rulestopstandby, packetfluxStandbypowerAllObjects=packetfluxStandbypowerAllObjects, rulereturnprimary=rulereturnprimary, webcontrol2=webcontrol2, ac2frequency=ac2frequency, webcontrol4=webcontrol4, webcontrol6=webcontrol6, relay1on=relay1on, numberofstarts=numberofstarts, switch3closed=switch3closed, totaltimeonprimary=totaltimeonprimary, currentstandbyruntime=currentstandbyruntime, relay5on=relay5on, webcontrol7=webcontrol7, totalunsuccessfulstarts=totalunsuccessfulstarts, shuntvoltage=shuntvoltage, recentstalls=recentstalls, pwr2voltage=pwr2voltage, currenttimeonstandby=currenttimeonstandby, webcontrol5=webcontrol5, rulestandbygood=rulestandbygood, switch4closed=switch4closed, enabled=enabled, powercontrollerstate=powercontrollerstate, standbypowerConformance=standbypowerConformance, mtr1voltage=mtr1voltage, mtr2voltage=mtr2voltage, PYSNMP_MODULE_ID=standbypower, ruleswitchstandby=ruleswitchstandby, ruleexercisestandby=ruleexercisestandby, laststandbyfailure=laststandbyfailure, totalstalls=totalstalls, ac1frequency=ac1frequency, temperature=temperature, webcontrol3=webcontrol3, pwr1voltage=pwr1voltage, relay3on=relay3on, relay4on=relay4on, relay2on=relay2on, switch5closed=switch5closed, totaltimeonstandby=totaltimeonstandby, ac1voltage=ac1voltage, laststandbyunsuccessfulstart=laststandbyunsuccessfulstart, totalstandbyruntime=totalstandbyruntime, standbypower=standbypower, switch1closed=switch1closed, transferswitchstate=transferswitchstate, webcontrol1=webcontrol1, ac2voltage=ac2voltage, relay7on=relay7on, switch2closed=switch2closed, numberoftransfers=numberoftransfers, laststandbygracefulstop=laststandbygracefulstop, webcontrol8=webcontrol8, relay6on=relay6on, standbypowerGroups=standbypowerGroups, recentunsuccessfulstarts=recentunsuccessfulstarts, currenttimeonprimary=currenttimeonprimary, standbypowerstate=standbypowerstate, laststandbyrun=laststandbyrun)
